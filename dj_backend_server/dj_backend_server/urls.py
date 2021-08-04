import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import user_login, user_logout


urlpatterns = [
    path("api/login/", user_login),
    path("api/logout/", user_logout),
    path("api/gps/", include("driver_car_app.urls"), name="car_gps_records"),
    path('admin/', admin.site.urls),
    path("__debug__", include(debug_toolbar.urls)),
]
