from django.urls import path
from .views import GpsListView, api_get_newest_location

urlpatterns = [
    path("gps/", GpsListView.as_view()),
    path("gps/newest/<truck_name>", api_get_newest_location, name="newest_gps")
]