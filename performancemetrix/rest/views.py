from django.shortcuts import render
from rest_framework.generics import ListAPIView
from performancemetrix.models import PerformanceMatrix
from .serializers import  PerformanceMatrixSerializer
from .filters import  PerformanceMatrixFilter

#Below class used for lsiting data of api with mix and match between filterset
#From django-filter and rest_framework filter
class PerformanceMatrixListAPIView(ListAPIView):
    serializer_class = PerformanceMatrixSerializer
    queryset = PerformanceMatrix.objects.calculated_quantity()
    fields=('id','date','channel','country','os','impressions','clicks','installs','spend','revenue','metric_cpi')
    filterset_class=(PerformanceMatrixFilter)
    ordering_fileds=('id','date','channel','country','os','impressions','clicks','installs','spend','revenue','metric_cpi')
