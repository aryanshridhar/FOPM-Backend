from rest_framework import generics, mixins
from .serializers import OrganizationSerializer, ProjectSerializer
from .models import Organization, Project
from rest_framework.permissions import IsAuthenticated


class CreateOrganization(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class CreateProject(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
