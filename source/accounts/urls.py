from django.urls import path
from accounts.views import login_view, logout_view, register_view, UserDetailView


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create", register_view, name="create"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail")

]

app_name = "accounts"

