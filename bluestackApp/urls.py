from django.contrib import admin
from django.urls import path, include
from bluestackApp.views import (
    UserSignupView,
    UserLoginView,
    EmpoloyeeCreateView,
    EmployeeDetailView, 
    EmployeeUpdateView,
    EmployeeDeleteView,
    RoomCreateView,
    RoomDetailView, 
    RoomUpdateView,
    RoomDeleteView,
    )

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),
    path('user-login-view/',UserLoginView.as_view()),
    path('create-employee/',EmpoloyeeCreateView.as_view()),
    path('employee-detail/',EmployeeDetailView.as_view()),
    path('employee-update/<int:pk>',EmployeeUpdateView.as_view()),
    path('employee-delete/<int:pk>',EmployeeDeleteView.as_view()),
    path('create-room/',RoomCreateView.as_view()),
    path('room-detail/',RoomDetailView.as_view()),
    path('room-detail-update/<int:pk>',RoomUpdateView.as_view()),
    path('room-delete/<int:pk>',RoomDeleteView.as_view()),
    
]