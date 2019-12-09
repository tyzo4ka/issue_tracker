from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Project, Issue
from api.serializers import ProjectSerializer, IssueSerializer, RegistrationSerializer
from rest_framework.permissions import DjangoModelPermissions, AllowAny


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered a new user"
        else:
            data = serializer.errors
        return Response(data)


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
