from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'department_code', 'description']





# class DepartmentSerializer(serializers.ModelSerializer):
#     # class Meta:
#     #     model = Department
#     #     fields = ['name', 'code', 'description']
#
#     name = serializers.CharField(max_length=255, required=True)
#     code = serializers.CharField(max_length=255, required=True)
#     description = serializers.CharField(max_length=255, required=False)
#
#
#
# class DepartmentGetSerializer(serializers.Serializer):
#     code = serializers.CharField(max_length=255, required=True)
#
# class DepartmentDeleteSerializer(serializers.Serializer):
#     code = serializers.CharField(max_length=255, required=True)
#
#
# class DepartmentUpdateSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255, required=False)
#     code = serializers.CharField(max_length=255, required=True)
#     description = serializers.CharField(max_length=255, required=False)