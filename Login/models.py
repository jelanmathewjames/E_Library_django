from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    forgot_password = models.CharField(max_length=100,null=True,blank=True)
    date_joined = models.DateTimeField(null=True,blank=True)
    last_login = models.DateTimeField(null=True,blank=True)
    last_logout = models.DateTimeField(null=True,blank=True)
    book1 = models.JSONField(null=True,blank=True)
    book2 = models.JSONField(null=True,blank=True)
    book3 = models.JSONField(null=True,blank=True)
    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','mobile']