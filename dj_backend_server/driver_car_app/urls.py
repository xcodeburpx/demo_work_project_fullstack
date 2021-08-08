from django.urls import path
from .views import get_truck_newest, get_truck_list

# Defined REST URIs for requests
urlpatterns = [
    path("newest/<truck_name>/", get_truck_newest, name="truck_newest"),
    path("truck_list/", get_truck_list, name="truck_list"),
]
