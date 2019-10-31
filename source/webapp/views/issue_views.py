from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from webapp.forms import IssueForm
from webapp.models import Issue
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


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = "issue/create.html"
    form_class = IssueForm

    def get_success_url(self):
        return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issue/update.html"
    context_object_name = "issue"

    def get_success_url(self):
        return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    form_class = IssueForm
    template_name = "issue/delete.html"
    model = Issue
    success_url = reverse_lazy("webapp:index")
    context_object_name = "issue"
