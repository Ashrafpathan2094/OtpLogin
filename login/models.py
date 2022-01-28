import imp
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User



# Create your models here.

class User_Mobile(models.Model):
    phone_number = models.CharField(max_length=12)
    otp = models.CharField(max_length=6)

class UserProfile(AbstractUser):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    User_Mobile = models.OneToOneField(User_Mobile,on_delete=models.CASCADE)
    dob = models.DateField(null=True) 
    gender = models.CharField(max_length=1, choices=GENDERS,blank=True,    null=True)
