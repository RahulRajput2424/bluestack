from django.contrib import admin
from django.urls import path, include
from bluestackApp.views import UserSignupView

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),
    
]