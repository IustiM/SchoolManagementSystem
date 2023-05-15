from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import Student
from .models import Class, Enrollment
from .serializers import ClassSerializer, EnrollmentSerializer


class ClassListView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        # if request.accepted_renderer.format == 'json':
        #     return Response(serializer.data)
        # elif request.accepted_renderer.format == 'html':
        return render(request, 'class_list.html', {'classes': serializer.data})


# @api_view(('GET',))
# @renderer_classes((JSONRenderer,))
class ClassDetail(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'classes/class_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        class_obj = get_object_or_404(Class, pk=pk)
        serializer = ClassSerializer(class_obj)
        data = serializer.data
        if request.accepted_renderer.format == 'html':
            print(data)
            context = {'class_obj': data}
            return render(request, self.template_name, context=context)
        return Response(data)


class ClassView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    serializer_class = ClassSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return Class.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.lookup_url_kwarg)
        if pk is not None:
            instance = self.get_queryset().get(pk=pk)
            serializer = self.serializer_class(instance)
            return Response(serializer.data, template_name='class_detail.html')
        classes = self.get_queryset()
        context = {'classes': classes}
        return render(request, 'class_list.html', context)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs.get(self.lookup_url_kwarg))
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=self.kwargs.get(self.lookup_url_kwarg))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EnrollmentView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'classes/enroll_students.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['students'] = Student.objects.all()
        context['classes'] = Class.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            context = self.get_context_data()
            return render(request, self.template_name, context)
        else:
            enrollments = Enrollment.objects.all()
            serializer = EnrollmentSerializer(enrollments, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            enrollment = Enrollment.objects.get(pk=pk)
        except Enrollment.DoesNotExist:
            raise Http404

        serializer = EnrollmentSerializer(enrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            enrollment = Enrollment.objects.get(pk=pk)
        except Enrollment.DoesNotExist:
            raise Http404

        enrollment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
