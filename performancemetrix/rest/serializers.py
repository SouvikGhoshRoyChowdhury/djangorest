from rest_framework import serializers
from performancemetrix.models import PerformanceMatrix

#Overriding __init__ of serializer to filter url based on fields in model
class DynamicPerformanceMatrixSerializer(serializers.ModelSerializer):
    def __init__(self,*args,**kwargs):
        super( DynamicPerformanceMatrixSerializer,self).__init__(*args,**kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())

            for field_name in existing - allowed:
                self.fields.pop(field_name)

#Actual serializer class which inherits above with declared fields
class PerformanceMatrixSerializer(DynamicPerformanceMatrixSerializer,serializers.ModelSerializer):
    date=serializers.DateField(format='%d-%m-%Y',required=False)
    channel=serializers.CharField(max_length=255,required=False)
    country=serializers.CharField(max_length=255,required=False)
    os=serializers.CharField(max_length=255,required=False)
    impressions=serializers.IntegerField(required=False)
    clicks=serializers.IntegerField(required=False)
    installs=serializers.IntegerField(required=False)
    spend=serializers.FloatField(required=False)
    revenue=serializers.FloatField(required=False)
    metric_cpi=serializers.DecimalField(max_digits=8,decimal_places=2,required=False)

    class Meta:
        model = PerformanceMatrix
        fields=('id','date','channel','country','os','impressions','clicks','installs','spend','revenue','metric_cpi')
