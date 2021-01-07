from django.contrib import admin
from django.urls import path, include
from bluestackApp.views import UserSignupView,UserLoginView,EmpoloyeeCreateView,EmployeeDetailView

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),
    path('user-login-view/',UserLoginView.as_view()),
    path('create-employee/',EmpoloyeeCreateView.as_view()),
    path('employee-detail/',EmployeeDetailView.as_view()),
   
]