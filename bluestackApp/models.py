from django.db import models
from django.contrib.auth.models import AbstractUser
from bluestackApp.CommonEnum import UserType, RoomStatus
class User(AbstractUser):
    user_type = models.CharField(choices=UserType.CHOICES,default=None,max_length=UserType.MAX_LENGTH,blank=True,null=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True, unique=True)
    mobileNumber = models.CharField(null=True,max_length=18, unique=True)
    position = models.CharField(null=True, max_length=50)
    team = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class ConfRoom(models.Model):
    name = models.CharField(max_length=255,unique=True)
    bookingMail =  models.EmailField(db_index=True, unique=True)
    sitting = models.CharField(null=False,max_length=18,blank=False)
    currentStatus = models.CharField(choices=RoomStatus.CHOICES,default=RoomStatus.AVAILABLE,max_length=UserType.MAX_LENGTH,blank=False,null=False)



