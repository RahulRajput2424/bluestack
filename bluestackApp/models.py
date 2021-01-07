from django.db import models
from django.contrib.auth.models import AbstractUser
from bluestackApp.CommonEnum import UserType
class User(AbstractUser):
    user_type = models.CharField(choices=UserType.CHOICES,default=None,max_length=UserType.MAX_LENGTH,blank=True,null=True)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True, unique=True)
    mobileNumber = models.CharField(null=True,max_length=18, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
