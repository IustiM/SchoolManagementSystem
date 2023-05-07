from rest_framework import serializers

from students.serializers import StudentSerializer, AttendanceSerializer
from teachers.serializers import TeacherSerializer
from .models import Class, Enrollment, Schedule


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    attendance = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'class_obj', 'enrollment_date']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['day_of_week', 'start_time', 'end_time']


class ClassSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(read_only=True)
    schedule = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'code', 'teacher', 'students', 'enrollments', 'schedule']


class EnrollmentDetailSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class_obj = ClassSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'class_obj', 'enrollment_date']
