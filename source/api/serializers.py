from webapp.models import Project, Issue
from rest_framework import serializers
from accounts.models import User


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


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "password_confirm", "email")
        extra_kwargs = {'password': {"write_only": True}}

    def save(self):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data["email"])
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords didn't match"})

        user.set_password(password)
        user.save()
        return user


