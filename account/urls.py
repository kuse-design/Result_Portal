from django.urls import path
from . import views



urlpatterns = [
    path('enroll-student/', views.StudentEnrollment.as_view(),name="enroll-student"),
    path('staff-enroll/', views.StaffEnrollment.as_view(),name="staff-enroll"),
]