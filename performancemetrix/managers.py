from django.db import models
from .models import *

from django.db.models import F,ExpressionWrapper
from django.db.models import DecimalField

#Adding custom queryset method for calculating cost per install to be used by manger class below
class PerformanceMatrixQuerySet(models.QuerySet):

    def calculated_quantity(self):
        return self.model.objects.annotate(
         metric_cpi=ExpressionWrapper(
         (F('spend')/F('installs')),
         output_field=DecimalField()
        ))

#This is custom manger class for model PerformanceMatrix
class PerformanceMatrixManager(models.Manager):
    def get_queryset(self):
        return PerformanceMatrixQuerySet(self.model,using=self._db)

    def calculated_quantity(self):
        return self.get_queryset().calculated_quantity()
