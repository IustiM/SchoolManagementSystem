from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('signup/', Signup.as_view(), name='Signup'),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('profile/', Profile.as_view(), name='Profile'),
    path('api/new_users/', NewUserList.as_view()),
    path('api/new_users/<int:pk>/', NewUserDetail.as_view()),
    path('api/managers/', CustomAccountManagerList.as_view()),
    path('api/managers/<int:pk>/', CustomAccountManagerDetail.as_view()),
]
