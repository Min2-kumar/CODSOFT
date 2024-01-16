from django.db import models

class Directory(models.Model):
    profilepic = models.ImageField(upload_to='profilepic')
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField(max_length=70)
    address = models.CharField(max_length=150)
    comment = models.CharField(max_length=250)