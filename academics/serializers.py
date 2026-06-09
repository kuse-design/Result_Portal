from rest_framework import serializers

from academics.models import Course, AcademicSession
from core.constants import LEVEL_CHOICES, SEMESTER_CHOICES


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('code', 'title', 'credit_units', 'level', 'semester', 'description')

    def create(self, validated_data):
        department_id = self.context.get('department_id')
        return Course.objects.create(department_id=department_id, **validated_data)

class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ('name', 'year', 'semester', 'is_current', 'start_date', 'end_date')






'''
{
 "code": "EEE111",
 "title": "electrical engineering",
 "credit_units": 3,
 "level": "100",
 "semester": "first",
 "description": "Introduction to electrical engineering"
}
'''