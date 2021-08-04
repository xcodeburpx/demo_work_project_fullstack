from django.contrib.auth import login
from django.db import reset_queries
from .models import Gps
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
# TODO:
# Protect these requests - add is authenticated closure/decorator
@login_required
def gps_get_all(request):
    if request.method == "GET":
        data = {
            "data_one": "data 1",
            "data_two": "data 2"
        }
        return JsonResponse({"wagadugu": "ukulele"})
