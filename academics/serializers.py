from rest_framework import serializers

from academics.models import Course, AcademicSession
from core.models import Department



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code', 'title', 'description', 'semester', 'level','credit_units']


    def create(self, validated_data):
        department_id = self.context.get('department_id')
        return Course.objects.create(department_id=department_id, **validated_data)


class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ['name', 'year', 'is_current', 'start_date', 'end_date']












