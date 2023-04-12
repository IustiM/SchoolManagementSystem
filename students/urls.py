from django.urls import path
from .views import StudentList, StudentDetail, AttendanceList, AttendanceDetail

app_name = 'students'

urlpatterns = [
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
    path('attendance/', AttendanceList.as_view(), name='attendance_list'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='attendance_detail'),
]
