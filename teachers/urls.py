from django.urls import path

from . import views

urlpatterns = [
    path('teachers/', views.TeacherList.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/create_exam/', views.CreateExam.as_view(), name='create_exam'),
    path('teachers/<int:pk>/view_exam/', views.ViewExam.as_view(), name='view_exam'),
]
