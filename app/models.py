from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    is_tailor = models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    address = models.TextField(null=True)
    phone_no = models.CharField(max_length=25,null=True)
