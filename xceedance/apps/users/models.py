from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)


class User(AbstractUser):
    employee_id = models.CharField(max_length=50)
    department = models.ForeignKey('users.Department', related_name='department_users', null=True, blank=True)
