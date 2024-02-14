from django.db import models

# Create your models here.

class RollingAvgModel():
    ticker = models.CharField(max_length=4, unique=True)
    prediction = models.IntegerField(null=False, default=1)

class RollingAvgBot():
    pass

class Login():
    email = models.CharField()
    password = models.CharField()