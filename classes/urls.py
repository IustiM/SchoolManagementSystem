from django.urls import path

from . import views
from .views import ClassView, EnrollmentView, ClassListView

app_name = 'classes'

urlpatterns = [
    path('classes/', ClassListView.as_view(), name='class_list'),
    path('classes/<int:pk>/', views.ClassDetail.as_view(), name='class_detail'),
    path('classes_detail/<int:pk>/', ClassView.as_view(), name='class_detail_view'),
    path('enroll_students/', EnrollmentView.as_view(), name='enroll_students'),
]

# urlpatterns = [
#     path('classes/<int:pk>/', ClassDetail.as_view(), name='class_detail'),
#     path('classes_list/', ClassView.as_view(), name='class_list'),
#     path('classes_detail/<int:pk>/', ClassView.as_view(), name='class_detail_view'),
#     path('enroll_students/', EnrollmentView.as_view(template_name='enroll_students.html'), name='enroll_students'),
#     ]
