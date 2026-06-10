from django.urls import include, path
from rest_framework import routers

from academics.views import AcademicSessionViewSet, CourseRegistrationViewSet

router = routers.DefaultRouter()
router.register('academic-sessions', AcademicSessionViewSet, basename='academic-sessions')
router.register('course-registrations', CourseRegistrationViewSet, basename='course-registrations')

urlpatterns = [
    # path('academic-session/', include(router.urls)),
    path('', include(router.urls)),
]