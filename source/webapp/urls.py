from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, IssueView, IssueUpdateView, IssueCreateView, IssueDeleteView, StatusView, \
    TypeView, StatusCreateView, TypeCreateView, StatusUpdateView, TypeUpdateView, TypeDeleteView, StatusDeleteView,\
    ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path("issue/add/", IssueCreateView.as_view(), name="issue_add"),
    path('issue/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_update'),
    path("issue/<int:pk>/delete", IssueDeleteView.as_view(), name="issue_delete"),
    path("statuses/all", StatusView.as_view(), name="all_statuses"),
    path("statuses/add/", StatusCreateView.as_view(), name="status_add"),
    path('statuses/<int:pk>/edit/', StatusUpdateView.as_view(), name="status_update"),
    path("types/all", TypeView.as_view(), name="all_types"),
    path("types/add", TypeCreateView.as_view(), name="type_add"),
    path("types/<int:pk>/edit/", TypeUpdateView.as_view(), name="type_update"),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name="status_delete"),
    path('types/<int:pk>/delete/', TypeDeleteView.as_view(), name="type_delete"),
    path("projects/all", ProjectView.as_view(), name="all_projects"),
    path("projects/<int:pk>", ProjectDetailView.as_view(), name="project_view"),
    path("projects/add", ProjectCreateView.as_view(), name="project_add"),
    path("projects/<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete")
]

app_name = "webapp"