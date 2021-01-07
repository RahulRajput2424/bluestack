from django.contrib import admin
from django.urls import path, include
from bluestackApp.views import UserSignupView,UserLoginView,EmpoloyeeCreate

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),
    path('user-login-view/',UserLoginView.as_view()),
    path('create-employee/',EmpoloyeeCreate.as_view()),
   
]