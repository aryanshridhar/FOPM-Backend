from rest_framework import generics, mixins
from .serializers import OrganizationSerializer, ProjectSerializer, RelOrgToUserModelSerializer, RelProjectToUserModelSerializer
from .models import Organization, Project, RelOrgToUserModel, RelProjectToUserModel
from rest_framework.permissions import IsAuthenticated


class CreateOrganization(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        organization = Organization.objects.create(name = serializer.data['name'], description = serializer.data['description'])
        user_instance = RelOrgToUserModel(organization = organization, user = self.request.user)
        user_instance.save()


class CreateProject(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        org = Organization.objects.get(name = serializer.data['organization'])
        project = Project.objects.create(organization = org, name = serializer.data['name'], description = serializer.data['description'])
        user_instance = RelProjectToUserModel(project = project, user = self.request.user)
        user_instance.save()


class RetrieveOrganization(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    serializer_class = RelOrgToUserModelSerializer

    def get_queryset(self):
        user = self.request.user
        model = RelOrgToUserModel.objects.filter(user = self.request.user)
        print(model)
        return model

class RetrieveProject(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = RelProjectToUserModelSerializer

    def get_queryset(self):
        user = self.request.user
        model = RelProjectToUserModel.objects.filter(user = self.request.user)
        return model
