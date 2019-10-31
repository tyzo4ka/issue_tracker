from django.urls import path
from accounts.views import login_view, logout_view, register_view, UserDetailView, UserPersonalInfoChangeView, \
    UserPasswordChangeView, AllUsersView, update_profile


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create", register_view, name="create"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
    path("<int:pk>/update", update_profile, name="update"),
    # path("<int:pk>/update", UserPersonalInfoChangeView, name="update"),
    path("<int:pk>/change_password", UserPasswordChangeView.as_view(), name="change_password"),
    path('all/', AllUsersView.as_view(), name="users")

]

app_name = "accounts"

