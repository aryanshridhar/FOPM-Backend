from rest_framework import serializers
from .models import Organization, Project, RelOrgToUserModel, RelProjectToUserModel


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class RelOrgToUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelOrgToUserModel
        fields = "__all__"

class RelProjectToUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelProjectToUserModel
        fields = "__all__"