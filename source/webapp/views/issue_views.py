from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic.base import View

from webapp.forms import IssueForm
from webapp.models import Issue, Project
from accounts.models import Team
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .base import SearchView


class IndexView(SearchView):
    context_object_name = 'issues'
    model = Issue
    template_name = 'issue/index.html'
    ordering = ['-created_date']
    paginate_by = 3
    paginate_orphans = 1

    def get_query(self):
        return Q(summary__icontains=self.search_query) | Q(description__icontains=self.search_query)


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_object_name = "issue"
    model = Issue


class UserPassesCheck(View):

    def check(self, project_pk, user_name):
        project = Project.objects.filter(pk=project_pk)
        teams = project[0].teams.all()
        # teams = project[0].projects.all()
        for user in teams:
            return user_name == user.user


class IssueCreateView(UserPassesCheck, CreateView):
    model = Issue
    template_name = "issue/create.html"
    form_class = IssueForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_pk = self.kwargs.get('pk')
        project = Project.objects.filter(teams__user=self.request.user)
        kwargs['projects'] = project
        return kwargs

    def form_valid(self, form):
        project_pk = self.request.POST.get('project')
        check = self.check(project_pk, self.request.user)
        if check:
            return super().form_valid(form)
        return HttpResponseForbidden("Access is denied")

    def get_success_url(self):
        return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})


class IssueUpdateView(UserPassesCheck, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issue/update.html"
    context_object_name = "issue"

    def get(self, *args, **kwargs):
        project_pk = self.get_object().project.pk
        check = self.check(project_pk, self.request.user)
        if check:
            return super().get(self.request)
        return HttpResponseForbidden("Access is denied")

    def get_success_url(self):
        return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})


class IssueDeleteView(UserPassesCheck, DeleteView):
    form_class = IssueForm
    template_name = "issue/delete.html"
    model = Issue
    success_url = reverse_lazy("webapp:index")
    context_object_name = "issue"

    def get(self, *args, **kwargs):
        project_pk = self.get_object().project.pk
        check = self.check(project_pk, self.request.user)
        if check:
            return super().get(self.request)
        return HttpResponseForbidden("Access is denied")
