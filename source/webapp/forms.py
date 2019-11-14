from django import forms
from webapp.models import Issue, Status, Type, Project, User
from accounts.models import Team


class IssueForm(forms.ModelForm):

    def __init__(self, **kwargs):
        self.projects = kwargs.pop('projects')
        print("Self projects", self.projects)
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(teams__project__in=self.projects)

    class Meta:
        model = Issue
        exclude = ["created_date", "updated_at", "created_by"]


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["state"]


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["name"]


class ProjectForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Project
        fields = ['name', 'description', 'users']


class ProjectIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["summary", "description"]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Find")


class ProjectAddUserForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)
    # def __init__(self, user, **kwargs):
    #     super().__init__(**kwargs)
    #     self.fields['user'].queryset = User.objects.all()

    class Meta:
        model = User
        fields = ['user']


class ProjectDeleteUserForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)

    def __init__(self, project_pk, **kwargs):
        super().__init__(**kwargs)
        self.fields['users'].queryset = Team.objects.filter(project=project_pk)

    class Meta:
        model = User
        fields = ['users']
