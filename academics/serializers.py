from rest_framework import serializers

from academics.models import Course
from core.models import Department



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code', 'title', 'description', 'semester', 'level','credits_units']


    def create(self, validated_data):
        department_id = self.context('department_id')
        return Course.objects.create(department_id=department_id, **validated_data)












    # def create(self, validated_data):
    #     department_id = self.context.get('department_id')
    #     department = Department.objects.get(pk=department_id)
    #     return Course.objects.create(department=department, **validated_data)