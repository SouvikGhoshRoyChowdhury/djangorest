from django_filters import rest_framework as rfilters
from performancemetrix.models import PerformanceMatrix
from django.db.models import Sum,F,ExpressionWrapper,DecimalField
from datetime import date

#Filterset implementing all feature requested as per question
class PerformanceMatrixFilter(rfilters.FilterSet):

    class Meta:
        model = PerformanceMatrix
        fields=['id','date','channel','country','os','impressions','clicks','installs','spend','revenue']

    for field in ['impressions','clicks','installs','spend','revenue']:
        exec(f'max_{field}=rfilters.NumberFilter(field,lookup_expr="gte")')
        exec(f'min_{field}=rfilters.NumberFilter(field,lookup_expr="lte")')

    date_to = rfilters.CharFilter(method='helper_date_to',label='date_to')
    date_from = rfilters.CharFilter(method='helper_date_from',label='date_from')

    date = rfilters.CharFilter(method='date_exact',label='date')
    groupby=rfilters.CharFilter(method='groupby_filter',label='groupby')

    field=rfilters.CharFilter(method='groupby_filter',label='field')

    def helper_date_to(self,queryset,name,value):
        day,month,year = self.date_split(value)
        actual_date = date (year,month,day)
        return queryset.filter(date__lte = actual_date)


    def helper_date_from(self,queryset,name,value):
        day,month,year = self.date_split(value)
        actual_date = date (year,month,day)
        return queryset.filter(date__gte = actual_date)


    def date_exact(self,queryset,name,value):
        day,month,year = self.date_split(value)
        actual_date = date (year,month,day)
        return queryset.filter(date = actual_date)

    def date_split(self,value):
        return [int(x) for x in value.split('-')]

    def groupby_filter(self,queryset,name,value):
        return queryset.values(*self.request.query_params.getlist('groupby')).annotate(
               impressions=Sum('impressions'),
               clicks=Sum('clicks'),
               installs=Sum('installs'),
               spend=Sum('spend'),
               revenue=Sum('revenue'),
               metric_cpi=ExpressionWrapper(
                (F('spend')/F('installs')),
                output_field=DecimalField())
        )
