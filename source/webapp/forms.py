from django import forms
from webapp.models import Issue, Status, Type, Project


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ["created_date"]


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["state"]


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["name"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_date', 'updated_date']


class ProjectIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["summary", "description"]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Find")


