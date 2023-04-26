from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Attendance
from .serializers import StudentSerializer, AttendanceSerializer


#
# def register_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             return redirect('student_detail', pk=student.pk)
#     else:
#         form = StudentForm()
#     return render(request, 'students/register_student.html', {'form': form})
#
#
# def student_detail(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     attendance = Attendance.objects.filter(student=student).order_by('date')
#     return render(request, 'students/student_detail.html', {'student': student, 'attendance': attendance})
#
#
# def student_attendance(request, pk):
#     student = get_object_or_404(Student, pk)
#     if request.method == 'POST':
#         date = request.POST.get('date')
#         is_present = request.POST.get('is_present') == 'on'
#         attendance = Attendance.objects.filter(student=student, date=date, is_present=is_present)
#         attendance.save()
#         return redirect('student_detail', pk=pk)
#     else:
#         return render(request, 'students/student_attendance.html', {'student': student})


class StudentList(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'students/student_list.html'

    def get(self, request, format=None):
        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        return Response({"students": serializers.data})

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentDetail(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'students/student_detail.html'

    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response({"students": serializer.data})

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttendanceList(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'students/student_attendance.html'

    def get_object(self, pk):
        return get_object_or_404(Attendance, pk=pk)

    def get(self, request, format=None):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response({"students": serializer.data})

    def post(self, request, format=None):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceDetail(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'students/student_detail.html'

    def get_object(self, pk):
        return get_object_or_404(Attendance, pk=pk)

    def get(self, request, pk, format=None):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance.data)
        return Response({"students": serializer.data})

    def put(self, request, pk, format=None):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        attendance = self.get_object(pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# <td><a href="{% url 'student_detail' student.id %}">View Profile</a></td>
