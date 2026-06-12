from rest_framework.permissions import AllowAny, IsAuthenticated
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
    serializer_class = CourseRegistrationSerializer
    permissions = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user

        qs = CourseRegistration.objects.select_related(
            "student__user", "course__department", "session"
        ).all()

        if user.is_active:
            qs = qs.filter(student=user.student_profile)

        return qs

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = self.request.user

        if user.is_authenticated and user.is_active:
            try:
                context["student"] = user.student_profile
            except Exception as e:
                context["student"] = None

        return context

    def create(self, request, *args, **kwargs):
        if not request.user.is_active:
            logger.warning(
                f"Non-student user_id={request.user.id} attempted course registration"

            )
            return Response(
            data:{"error": "Only active students can register for course"}
            status=status.HTTP_400_FORBIDDEN,
            )

            try:
                student = request.user.student_profile
                


