from django.db import models

class Trader(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50, unique=False)
    password = models.CharField(max_length = 50)
