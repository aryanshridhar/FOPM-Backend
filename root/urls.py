from django.contrib import admin
from django.urls import path, include
from .views import CreateOrganization, CreateProject

urlpatterns = [
    path("create-org", CreateOrganization.as_view()),
    path("create-project", CreateProject.as_view()),
]
