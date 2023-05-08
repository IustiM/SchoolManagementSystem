from django.urls import path

from .views import ClassView, EnrollmentView, ClassDetail

urlpatterns = [
    path('classes/<int:pk>/', ClassDetail, name='class_detail'),
    path('classes_list/', ClassView.as_view(), name='class_list'),
    path('classes_detail/<int:pk>/', ClassView.as_view(), name='class_detail_view'),
    path('enroll_students/', EnrollmentView.as_view(template_name='enroll_students.html'), name='enroll_students'),
    ]


