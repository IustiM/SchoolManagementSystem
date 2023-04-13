from django.urls import path

from .views import *

urlpatterns = [
    path('api/new_users/', NewUserList.as_view()),
    path('api/new_users/<int:pk>/', NewUserDetail.as_view()),
    path('api/managers/', CustomAccountManagerList.as_view()),
    path('api/managers/<int:pk>/', CustomAccountManagerDetail.as_view()),
]
