from rest_framework import routers
from django.urls import path, include

from academics.views import AcademicSessionViewSet

router = routers.DefaultRouter()
router.register(r'', AcademicSessionViewSet, basename='academic-session')

urlpatterns = [
    path('', include(router.urls))
]