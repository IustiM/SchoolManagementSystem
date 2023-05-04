from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.TeacherList.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view(), name='teacher_detail'),
]
