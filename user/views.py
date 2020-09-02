import json
import requests

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from .models import User

class LogIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(password=data['password']).exists():
                user = User.objects.get(password=data['password']).name

                return JsonResponse({
                    'message':'success',
                    'user' : user}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)



