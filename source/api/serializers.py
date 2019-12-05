from webapp.models import Project, Issue
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_date', 'updated_at',
                  'created_by', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_date', 'updated_date', 'status', 'issues')

