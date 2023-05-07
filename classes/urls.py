from django.urls import path

from .views import ClassView, EnrollmentView

urlpatterns = [
    path('classes/', ClassView.as_view(), name='class_list'),
    path('classes/<int:pk>/', ClassView.as_view(), name='class_detail'),
    path('enrollments/', EnrollmentView.as_view(), name='enrollment_list'),
]
