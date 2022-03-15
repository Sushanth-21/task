from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
