from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import TeacherForm
from .models import Teacher, Attendance, Schedule, Course
from .serializers import TeacherSerializer, AttendanceSerializer, ScheduleSerializer, CourseSerializer


class TeacherList(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'teachers/teacher_list.html'

    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response({"teachers": serializer.data})

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TeacherDetail(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'teachers/teacher_detail.html'

    def get_object(self, pk):
        return get_object_or_404(Teacher, pk=pk)

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response({"teacher": serializer.data})

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
