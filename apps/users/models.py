from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField()
    birthday = models.DateField()
    mobile = models.CharField()
    gender = models.CharField()
    email = models.CharField()

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
