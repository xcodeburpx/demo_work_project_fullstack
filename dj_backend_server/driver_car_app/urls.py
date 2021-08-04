from django.urls import path
from .views import gps_get_all

# Defined REST URIs for requests
urlpatterns = [
    path("all_other/", gps_get_all, name="other_all_gps")
]
