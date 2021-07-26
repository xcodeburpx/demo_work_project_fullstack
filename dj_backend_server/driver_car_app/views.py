from .models import Gps
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GpsSerializer
from django.shortcuts import render

# Create your views here.

class GpsViewSet(viewsets.ModelViewSet):
    queryset = Gps.objects.all().order_by('timestamp')
    serializer_class = GpsSerializer
