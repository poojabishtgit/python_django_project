from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length = 80)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    address = models.TextField(max_length = 80)
    username = models.CharField(max_length = 80)
    password = models.CharField(max_length = 80)
