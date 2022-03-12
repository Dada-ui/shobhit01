from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class registermodel(User):
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=10, choices=[['Male','MALE'],['Female','FEMALE']])
    dor=models.DateTimeField(default=timezone.now)


class chatmodel(models.Model):
    cid = models.ForeignKey(registermodel,on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    datetime = models.DateTimeField(default=timezone.now)
    files = models.FileField(upload_to='chatdoc/',null=True)