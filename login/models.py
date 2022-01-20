import imp
from pyexpat import model
from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class user_mobile(models.Model):
    mobile = models.CharField(max_length=12)
    otp = models.CharField(max_length=6)

class profile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_mobile = models.OneToOneField(user_mobile,on_delete=models.CASCADE)
    dob = models.DateField(null=True) 
    gender = models.CharField(max_length=1, choices=GENDERS,blank=True,    null=True)
