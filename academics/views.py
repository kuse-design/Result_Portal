from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Course, AcademicSession, CourseRegistration
from .serializers import CourseSerializer, AcademicSessionSerializer, CourseRegistrationSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(department=self.kwargs["nested_1_pk"])

    def get_serializer_context(self):
        return {"department_id": self.kwargs.get("nested_1_pk")}


class AcademicSessionViewSet(ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer


class CourseRegistrationViewSet(ModelViewSet):
    queryset = CourseRegistration.objects.select_related(
        'student',
        'course',
        'session'
    )

    serializer_class = CourseRegistrationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = self.queryset

        student_id = self.request.query_params.get('student')
        session_id = self.request.query_params.get('session')

        if student_id:
            queryset = queryset.filter(student_id=student_id)

        if session_id:
            queryset = queryset.filter(session_id=session_id)

        return queryset