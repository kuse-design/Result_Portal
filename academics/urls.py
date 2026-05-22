
from .views import create_course
from django.urls import path


urlpatterns = [
path('create_course/', create_course, name='create_course'),
    ]