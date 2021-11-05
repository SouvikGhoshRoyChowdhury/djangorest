from django.urls import path
from .views import PerformanceMatrixListAPIView

urlpatterns = [
  path('rest/performancemetrix',PerformanceMatrixListAPIView.as_view())
]
