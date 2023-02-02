from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    is_tailor = models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    address = models.TextField(null=True)
    phone_no = models.CharField(max_length=25,null=True)

class DressCategory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
class Dress(models.Model):
    category = models.ForeignKey(DressCategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(null=True)
    photo = models.ImageField(upload_to='DressLists')

class Leave(models.Model):
    tailor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    submitted_on = models.DateField()
    approval = models.IntegerField(default=0)
