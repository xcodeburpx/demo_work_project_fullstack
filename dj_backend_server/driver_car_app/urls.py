from django.urls import path
from .views import GpsListView, api_get_newest_location

urlpatterns = [
    path("", GpsListView.as_view()),
    path("newest/<truck_name>", api_get_newest_location, name="newest_gps")
]