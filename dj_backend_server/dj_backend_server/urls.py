import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("gps/", include("driver_car_app.urls"), name="car_gps_records"),
    path('admin/', admin.site.urls),
    path("__debug__", include(debug_toolbar.urls)),
]
