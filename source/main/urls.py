"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, IssueView, IssueUpdateView, IssueCreateView, IssueDeleteView, StatusView, \
    TypeView, StatusCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path("issue/add/", IssueCreateView.as_view(), name="issue_add"),
    path('issue/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_update'),
    path("issue/<int:pk>/delete", IssueDeleteView.as_view(), name="issue_delete"),
    path("statuses/all", StatusView.as_view(), name="all_statuses"),
    path("statuses/add/", StatusCreateView.as_view(), name="status_add"),
    path("types/all", TypeView.as_view(), name="all_types")
]
