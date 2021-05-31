from django.db import models
from django.contrib.auth.models import User



class comm(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=250, verbose_name='کامنت')


class CSVFile(models.Model):
    file = models.FileField()