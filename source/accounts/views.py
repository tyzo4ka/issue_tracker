from pyexpat.errors import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, UpdateView, ListView

from .forms import UserCreationForm, UserChangeForm, PasswordChangeForm, ProfileForm


def login_view(request):
    context = {}
    next_page = request.GET.get('next')
    redirect_page = request.session.setdefault('redirect_page', next_page)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next_page:
                return redirect(redirect_page)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')


def register_view(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "user_create.html", {"form": form})
    elif request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data["username"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect('webapp:index')
        else:
            return render(request, "user_create.html", {"form": form})


class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user"


class UserPersonalInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = "user_update.html"
    form_class = UserChangeForm
    context_object_name = "user_obj"

    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"]

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


@login_required
@transaction.atomic
def update_profile(request, pk):
    user = User.objects.get(pk=pk)
    user.profile.git_profile = 'https://github.com/'
    user.save()
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:detail', pk=pk)
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = "user_change_password.html"
    form_class = PasswordChangeForm
    context_object_name = "user_obj"

    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"]

    def get_success_url(self):
        return reverse("accounts:login")


class AllUsersView(ListView):
    template_name = "all_users.html"
    context_object_name = "users"
    paginate_by = 20
    paginate_orphans = 2

    def get_queryset(self):
        return User.objects.all().order_by("username")
