from rest_framework import serializers
from account.models import Student
from account.serializers import StudentEnrollmentSerializer
from .models import Course, AcademicSession, CourseRegistration


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code', 'title', 'level', 'semester', 'description', 'credit_units']

    def create(self, validated_data):
        department_id = self.context.get('department_id')
        return Course.objects.create(department_id=department_id, **validated_data)


class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ['name', 'year', 'semester', 'is_current', 'start_date', 'end_date']


class CourseRegistrationSerializer(serializers.ModelSerializer):
    student = StudentEnrollmentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    session = AcademicSessionSerializer(read_only=True)

    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='student',
        write_only=True
    )

    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
        write_only=True
    )

    session_id = serializers.PrimaryKeyRelatedField(
        queryset=AcademicSession.objects.all(),
        source='session',
        write_only=True
    )

    class Meta:
        model = CourseRegistration
        fields = ["id", "student", "course", "session", "student_id", "course_id", "session_id", "register_at"]
        read_only_fields = ["register_at"]

    def validate(self, attrs):
        student = attrs.get('student')
        course = attrs.get('course')
        session = attrs.get('session')

        exists = CourseRegistration.objects.filter(
            student=student,
            course=course,
            session=session
        )

        if self.instance:
            exists = exists.exclude(pk=self.instance.pk)

        if exists.exists():
            raise serializers.ValidationError("Student already registered for the course")

        if course.semester != session.semester:
            raise serializers.ValidationError(
                f"{course.course_code} belongs "
                f"to {course.semester} semester"
            )

        return attrs