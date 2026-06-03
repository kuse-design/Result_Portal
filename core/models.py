from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import ForeignKey

from core.constants import ROLE_CHOICES, ROLE_ADMIN


class  User(AbstractBaseUser):

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default="student")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"

    def get_full_name(self):
        return f"{self.get_full_name} {self.last_name}".strip()

    @property
    def is_admin(self):
        return self.role == ROLE_ADMIN



class Department(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True, null=False)
    department_code = models.CharField(max_length=10, blank=False, unique=True, null=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_department'
        ordering = ['name']

    def __str__(self):
        return f"{self.department_code} {self.name}"

