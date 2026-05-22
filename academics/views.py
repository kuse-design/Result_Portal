from loguru import logger
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from academics.models import Course
from academics.serializers import CourseSerializer
from core.models import Department


@api_view(['POST'])
def create_course(request):
    try:
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        department_code = serializer.validated_data["department_code"]
        code = serializer.validated_data["code"]
        logger.info(f"data validated for course {code}")

        if not Department.objects.filter(code=department_code).exists():
            logger.error(f"Department with code {department_code} does not exist")
            return Response(
                {"message": f"Department with code {department_code} does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        if Course.objects.filter(code=code).exists():
            logger.error(f"Course with code {code} already exists")
            return Response(
                {"message": f"Course with code {code} already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        department = Department.objects.get(code=department_code)
        serializer.save(department=department)
        logger.info(f"Course {code} created successfully")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(f"Error creating course: {str(e)}")
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

