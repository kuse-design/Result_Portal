from rest_framework import serializers

from academics.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['department_code', 'code', 'title', 'credit_units', 'level', 'semester' ]