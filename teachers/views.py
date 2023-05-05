from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from .forms import *
from .serializers import TeacherSerializer


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
        user = request.user
        if user.is_superuser or teacher == user:
            return Response({'teacher': serializer.data})
        else:
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


class CreateExam(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'teachers/create_exam.html'
    success_url = reverse_lazy('view_exam')

    def get_initial(self):
        teacher = get_object_or_404(Teacher, pk=self.kwargs['pk'])
        return {'teacher': teacher}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ViewExam(ListView):
    model = Exam
    template_name = 'teachers/view_exam.html'
    context_object_name = 'exams'

    def get_queryset(self):
        teacher = get_object_or_404(Teacher, pk=self.kwargs['pk'])
        return Exam.objects.filter(teacher=teacher)
