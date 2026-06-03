from academics.views import CourseViewSet
from .views import DepartmentViewSet
from django.urls import path, include
# from rest_framework import routers
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('department', DepartmentViewSet, basename='department')
depat_router = routers.NestedDefaultRouter(router, r'department')
depat_router.register('course', CourseViewSet, basename='course')


urlpatterns = [
    path('', include(router.urls)),
    # path('department/create/', create_department, name='create_department'),
    # path('department/get/<str:code>/', get_department, name='get_departments'),
    # path('department/get/', get_department, name='get_all_departments'),
    # path('department/update/<str:code>/', update_department, name='update_department'),
    # path('department/delete/<str:code>/', delete_department, name='delete_department'),
]