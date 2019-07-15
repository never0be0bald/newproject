from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    is_active = models.BooleanField(default=0)
