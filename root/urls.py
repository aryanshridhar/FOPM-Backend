from django.contrib import admin
from django.urls import path, include
from .views import CreateOrganization, CreateProject, RetrieveOrganization, RetrieveProject

urlpatterns = [
    path("create-org", CreateOrganization.as_view()),
    path("create-project", CreateProject.as_view()),
    path("create-task", CreateTask.as_view()),
    path("get-task", RetrieveTask.as_view()),
    path("get-project", RetrieveProject.as_view()),
    path("get-orgs", RetrieveOrganization.as_view()),
]
