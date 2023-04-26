from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home.as_view(), name='home'),
    path('login/', login.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
    path('profile/', profile.as_view(), name='profile'),
    path('api/new_users/', NewUserList.as_view()),
    path('api/new_users/<int:pk>/', NewUserDetail.as_view()),
    path('api/managers/', CustomAccountManagerList.as_view()),
    path('api/managers/<int:pk>/', CustomAccountManagerDetail.as_view()),
]
