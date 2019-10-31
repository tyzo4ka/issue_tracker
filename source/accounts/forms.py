from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Username", required=True)
    password = forms.CharField(max_length=100, label="Password", required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label="Confirm Password", required=True,
                                       widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError("User with this username already exists", code="username_exists")

        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data["password_confirm"]
        data = self.cleaned_data
        if not data.get('first_name') and not data.get('last_name'):
            raise ValidationError("One of the following fields: first_name, last_name should be filled",
                                  code='first_name_last_name_criteria_empty')
        if password_1 != password_2:
            raise ValidationError("Passwords does not match", code="passwords_does_not_match")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists', code='user_email_exists')
        except User.DoesNotExist:
            return email

    class Meta:
        model = User
        fields = ['username', 'password', "password_confirm", 'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", 'last_name', 'email']
        labels = {'first_name': "First name", "last_name": "Last name", "email": "email"}


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="New password", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", strip=False, widget=forms.PasswordInput)
    old_password = forms.CharField(label="Old password", strip=False, widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid password.', code='invalid_password')
        return old_password

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match", code='passwords_do_not_match')

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['git_profile']
        labels = {"git_profile": "Git profile"}
