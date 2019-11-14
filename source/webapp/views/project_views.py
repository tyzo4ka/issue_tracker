from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from accounts.models import Team
from webapp.forms import ProjectForm, ProjectIssueForm, ProjectAddUserForm, ProjectDeleteUserForm
from webapp.models import Project, User
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .base import SearchView


class ProjectView(SearchView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/projects.html'
    ordering = ['created_date']
    paginate_by = 5
    paginate_orphans = 1

    def qet_query(self):
        return Q(name__icontains=self.search_query)


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    context_object_name = "project"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectIssueForm()
        issues = context['project'].issues.order_by("-created_date")
        self.paginate_issues_to_context(issues, context)
        pk = self.kwargs.get('pk')
        teams = Team.objects.filter(project_id=pk, end_date=None)
        print(teams)
        context['teams'] = teams
        users = User.objects.filter(teams__project=self.object)
        context["users"] = users
        return context

    def paginate_issues_to_context(self, issues, context):
        paginator = Paginator(issues, 5, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['issues'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = ProjectForm
    permission_required = 'webapp.add_project'
    permission_denied_message = "Access denied"

    def form_valid(self, form):
        users = form.cleaned_data.pop('users')
        self.object = form.save()
        start_date = datetime.now()
        pk = self.object.pk
        for user in users:
            Team.objects.create(user=user, project=self.object, start_date=start_date)
        self.add_author_to_project()
        return redirect('webapp:project_view', pk)

    def add_author_to_project(self):
        user = self.request.user
        project = self.object
        start_date = datetime.now()
        author = Team.objects.create(user=user, project=project, start_date=start_date)

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/update_project.html"
    context_object_name = "project"
    permission_required = 'webapp.change_project'
    permission_denied_message = "Access denied"

    def form_valid(self, form):
        users = form.cleaned_data.pop('users')
        self.object = form.save()
        start_date = datetime.now()
        pk = self.object.pk
        for user in users:
            Team.objects.create(user=user, project=self.object, start_date=start_date)
        return redirect('webapp:project_view', pk)

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    form_class = ProjectForm
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy("webapp:all_projects")
    context_object_name = "project"
    permission_required = 'webapp.delete_project'
    permission_denied_message = "Access denied"

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.form_class(data=request.POST)
    #     success_url = self.get_success_url()
    #     self.object.status.pk = 2
    #     self.object.save()
    #
    #     return HttpResponseRedirect(success_url)


class ProjectDeleteUser(PermissionRequiredMixin, DeleteView):
    model = Team
    template_name = "project/delete_user.html"
    context_object_name = "team"
    permission_required = 'webapp.delete_team'
    permission_denied_message = "Access denied"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        print(self.object)
        end_date = datetime.now()
        team = self.object
        print("End date", team.end_date)
        team.end_date = end_date
        team.save()
        print("End date", team.end_date)

        return HttpResponseRedirect(success_url)

    def user_delete_check(self, request, *args, **kwargs):
        project_pk = self.kwargs.get('pk')
        project = Team.objects.get(pk=project_pk)
        return project.user.pk == request.user.pk

    def get(self, request, *args, **kwargs):
        if self.user_delete_check(request, *args, **kwargs):
            return HttpResponseForbidden("Can't delete yourself from project")
        else:
            return super().get(self.request)
        # project_pk = self.kwargs.get('pk')
        # project = Team.objects.get(pk=project_pk)
        # if project.user.pk == request.user.pk:
        #     return HttpResponseForbidden("Can't delete yourself from project")
        # return super().get(self.request)

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.project.pk})

