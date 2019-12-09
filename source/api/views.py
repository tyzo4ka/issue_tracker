from rest_framework import viewsets
from webapp.models import Project, Issue
from api.serializers import ProjectSerializer, IssueSerializer
from rest_framework.permissions import DjangoModelPermissions


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
