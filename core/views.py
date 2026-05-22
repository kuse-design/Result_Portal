from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loguru import logger
from .models import Department
from .serializers import DepartmentSerializer


# Create your views here.

@api_view(['POST'])
def create_department(request):
    try:
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"]
        code = serializer.validated_data["code"]
        logger.info(f"data validated for department {name} ")

        if Department.objects.filter(code = serializer.validated_data["code"]).exists():
            logger.error(f"Department with code {code} already exists")
            return Response({"message":f"Department with code {code} already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        logger.info(f" department {name} created")
        return Response(serializer.data, status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(f"Error while creating department  {str(e)}")
        return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def get_department(request, code):
    try:
        department = Department.objects.filter(code=code)
        serializer = DepartmentSerializer(department)
        logger.info(f"Retrieved department with code {code}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Department.DoesNotExist:
        logger.error(f"Department with code {code} not found")
        return Response({"message": f"Department with code {code} not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error retrieving department: {str(e)}")
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT', 'PATCH'])
def update_department(request, code):
    try:
        department = Department.objects.get(code=code)
        is_partial = request.method == 'PUT'
        serializer = DepartmentSerializer(department, data=request.data, partial=is_partial)
        serializer.is_valid(raise_exception=True)

        new_code = serializer.validated_data.get("code")
        if new_code and new_code != department.code:
            if Department.objects.filter(code=new_code).exists():
                logger.error(f"Department with code {new_code} already exists")
                return Response({"message": f"Department with code {new_code} already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        logger.info(f"Department {code} updated successfully")
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Department.DoesNotExist:
        logger.error(f"Department with code {code} not found")
        return Response({"message": f"Department with code {code} not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error updating department: {str(e)}")
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_department(request, code):
    try:
        department = Department.objects.get(code=code)
        name = department.name
        department.delete()
        logger.info(f"Department '{name}' deleted")
        return Response({"message": f"Department '{name}' deleted successfully"}, status=status.HTTP_200_OK)

    except Department.DoesNotExist:
        logger.error(f"Department with code {code} not found")
        return Response({"message": f"Department with code {code} not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error deleting department: {str(e)}")
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



