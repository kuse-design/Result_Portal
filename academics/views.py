from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Course, AcademicSession
from .serializers import CourseSerializer, AcademicSessionSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_context(self):
        return {"department_id": self.kwargs.get("nested_1_pk")}


class AcademicSessionViewSet(ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer


# class AcademicSessionViewSet(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = AcademicSessionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)