from django.db import reset_queries
from .models import Gps
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GpsSerializer

# Create your views here.
class GpsListView(generics.ListAPIView):
    queryset = Gps.objects.all().order_by('timestamp')
    serializer_class = GpsSerializer


@api_view(["GET",])
def api_get_newest_location(request, truck_name):
    try:
        gps = Gps.objects.filter(truck__truck_name=truck_name).order_by("timestamp").first()
        if gps is None:
            raise Gps.DoesNotExist()
    except Gps.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GpsSerializer(gps)
        return Response(serializer.data)
