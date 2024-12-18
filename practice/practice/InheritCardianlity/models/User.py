from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField(null=True)


