from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'demo1'),
      (2, 'demo2'),
  )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES,default=None)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True, unique=True)
    mobileNumber = models.CharField(null=True,max_length=18, unique=True)