from .views import create_department, get_department, update_department
from django.urls import path


urlpatterns = [
    path('create_department/', create_department, name='create_department'),
    path('get_department/<str:code>', get_department, name='get_department'),
    path('update_department/<str:code>', update_department, name='update_department'),
    # path('delete_department/', delete_department, name='delete_department'),
]