from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:pk>/attendance/', views.student_attendance, name='student_attendance'),
]
