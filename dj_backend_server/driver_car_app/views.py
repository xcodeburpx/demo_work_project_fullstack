from django.db import reset_queries
from .models import Gps
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, \
                                          BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import GpsSerializer

# Create your views here.
# TODO:
# Protect these requests - add is authenticated closure/decorator
class GpsListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Gps.objects.all().order_by('timestamp')
    serializer_class = GpsSerializer


@api_view(["GET",])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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
