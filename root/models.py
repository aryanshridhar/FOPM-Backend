from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):

    name = models.CharField(max_length=256, primary_key=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Project(models.Model):

    organization = models.ForeignKey(to=Organization, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class RelOrgToUserModel(models.Model):

    organization = models.ForeignKey(to=Organization, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

class RelProjectToUserModel(models.Model):

    project = models.ForeignKey(to=Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)