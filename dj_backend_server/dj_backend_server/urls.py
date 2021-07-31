import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from .views import IndexView, MyTokenObtainPairView


urlpatterns = [
    path('', IndexView.as_view()),
    path('api/token/',
         MyTokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path("api/gps/", include("driver_car_app.urls"), name="car_gps_records"),
    path('admin/', admin.site.urls),
    path("__debug__", include(debug_toolbar.urls)),
]
