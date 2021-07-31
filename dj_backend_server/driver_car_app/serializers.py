from .models import Gps
from rest_framework import serializers


# Simple data serializer, it should be enough
class GpsSerializer(serializers.ModelSerializer):
    truck = serializers.StringRelatedField()

    class Meta:
        model = Gps
        fields = ['truck', 'timestamp', 'longitude', 'latitude', 'altitude']
