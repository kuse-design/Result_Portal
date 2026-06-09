from django.db import models

from core.constants import ROLE_STUDENT, LEVEL_CHOICES
from core.models import User, Department
from account.util import generate_matric_number

# Create your models here.
class Student(models.Model):

    STUDENT_STATUS_CHOICES = [
        ("active", "Active"),
        ("suspended", "Suspended"),
        ("graduated", "Graduated"),
        ("withdrawn", "Withdrawn"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile", limit_choices_to={"role": ROLE_STUDENT},
    )

    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="student_department")
    matric_number = models.CharField(max_length=20, unique=True, default=generate_matric_number, primary_key=True)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default="100")
    status = models.CharField(max_length=20, choices=STUDENT_STATUS_CHOICES, default="active",)
    entry_year = models.PositiveIntegerField()
    enrolled_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "student account"
        ordering = ["-matric_number"]

    def __str__(self):
        return f"{self.matric_number} - {self.user.get_full_name()}"

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status

class Staff(models.Model):
    DESIGNATION_CHOICES = [
        ("L1", "Lecturer I"),
        ("L2", "Lecturer II"),
        ("SLR", "Senior Lecturer"),
        ("PROF", "Professor"),
        ("HOD", "Head of Department"),
    ]

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    designation = models.CharField(max_length=4, choices= DESIGNATION_CHOICES, default= "L1", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.designation}"

    class Meta:
        ordering = ['designation']
