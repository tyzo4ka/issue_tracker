from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import IssueForm
from webapp.models import Issue
from django.views.generic import TemplateView, ListView


class IndexView(ListView):
    context_object_name = 'issues'
    model = Issue
    template_name = 'Issue/index.html'
    ordering = ['-created_date']
    paginate_by = 3
    paginate_orphans = 1


class DetailView(TemplateView):
    context_key = "objects"
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context


class IssueView(DetailView):
    template_name = 'Issue/issue.html'
    context_key = "issue"
    model = Issue


class IssueCreateView(ListView):

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, "Issue/create.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data["summary"],
                description=form.cleaned_data["description"],
                status=form.cleaned_data["status"],
                type=form.cleaned_data['type'])
            return redirect("issue_view", pk=issue.pk)
        else:
            return render(request, "Issue/create.html", context={'form': form})


class IssueUpdateView(ListView):

    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type
        })
        return render(request, 'Issue/update.html', context={
            'form': form,
            'issue': issue
        })

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type = form.cleaned_data['type']
            issue.save()
            return redirect("issue_view", pk=issue.pk)
        else:
            return render(request, "Issue/update.html", context={"form": form, "issue": issue})


class IssueDeleteView(ListView):
    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        return render(request, "Issue/delete.html", context={"issue": issue})

    def post(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        issue.delete()
        return redirect("index")