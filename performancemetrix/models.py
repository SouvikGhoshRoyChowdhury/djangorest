from django.db import models
from performancemetrix.managers import PerformanceMatrixQuerySet

# Create your models here.

class PerformanceMatrix(models.Model):
    date=models.DateField(auto_now=False)
    channel=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    os=models.CharField(max_length=255)
    impressions=models.IntegerField()
    clicks=models.IntegerField()
    installs=models.IntegerField()
    spend=models.FloatField()
    revenue=models.FloatField()
    #Declaring objects to use PerformanceMatrixQuerySet from managers.py as manager
    objects=PerformanceMatrixQuerySet.as_manager()
