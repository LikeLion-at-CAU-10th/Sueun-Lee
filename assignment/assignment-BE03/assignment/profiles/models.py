from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30, null= True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)

class URL(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.title
