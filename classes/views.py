from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from students.models import Student
from .models import Class, Enrollment
from .serializers import ClassSerializer, EnrollmentSerializer


class ClassListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    template_name = 'class_list.html'


class ClassView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    serializer_class = ClassSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return Class.objects.all()

    def get(self, request):
        classes = Class.objects.all()
        context = {'classes': classes}
        return render(request, 'class_list.html', context)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EnrollmentView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    template_name = 'enroll_students.html'

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return EnrollmentSerializer
    #     return EnrollmentDetailSerializer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        context['classes'] = Class.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        # enrollments = self.queryset
        enrollments = []
        context = {'enrollments': enrollments}
        return render(request, 'enroll_students.html', context)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def ClassDetail(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    context = {
        'class_obj': class_obj,
    }
    return render(request, 'class_detail.html', context)

# def enroll_students(request):
#     students = Student.objects.all()
#     classes = Class.objects.all()
#
#     if request.method == 'POST':
#
#         context = {
#             'students': students,
#             'classes': classes,
#         }
#     return render(request, 'enroll_students.html', context)
