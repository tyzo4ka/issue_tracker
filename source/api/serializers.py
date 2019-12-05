from webapp.models import Project, Issue
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_date', 'updated_date', 'status')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_date', 'updated_at',
                  'created_by', 'assigned_to')

