import json
from django.contrib.auth import login
from django.db import reset_queries
from .models import Gps, Truck
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

# Create your views here.
# TODO:
# Protect these requests - add is authenticated closure/decorator
@login_required
@require_http_methods(['GET', 'OPTIONS'])
def get_truck_list(request):
    if request.method == "GET":
        try:
            trucks = Truck.objects.values_list('truck_name', flat=True)
            trucks = list(trucks)
            return JsonResponse({'status': 'OK', 'data': trucks})
        except:
            return JsonResponse({'status': 'Something went wrong!'})



@login_required
@require_http_methods(['GET', 'OPTIONS'])
def get_truck_newest(request, truck_name):
    if request.method == "GET":
        try:
            gps_data = Gps.objects.filter(truck__truck_name=truck_name) \
                                  .order_by("timestamp") \
                                  .reverse() \
                                  .first()
            if gps_data is None:
                raise Gps.DoesNotExist()
            gps_data = model_to_dict(gps_data)
            gps_data["truck"] = truck_name
            gps_data.pop("id")
            return JsonResponse({'status': 'OK', 'data': gps_data})
        except Gps.DoesNotExist:
            return JsonResponse({'status': f'Data for truck {truck_name} does not exist'})
