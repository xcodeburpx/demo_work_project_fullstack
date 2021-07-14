from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import my_first_task

def index(request):
    my_first_task.delay(10)
    return HttpResponse('response done')