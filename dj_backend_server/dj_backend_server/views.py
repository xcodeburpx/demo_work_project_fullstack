import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['POST', 'OPTIONS'])
def user_login(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                data = {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }

                print(f'User {username} logged in')
                return JsonResponse({'status': 'OK', 'data': data})
            else:
                print(f'error: the username {username} or password is incorrect.')
                return HttpResponse(status=401, \
                                    content=f'The username {username} or password is incorrect.')
        else:
            return JsonResponse({'status': 'User already logged in'})


@require_http_methods(['GET', 'OPTIONS'])
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'status': 'OK'})
    else:
        return JsonResponse({'status': 'User already logged out'})
