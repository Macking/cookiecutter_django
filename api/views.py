from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Api
from api.serializers import ApiSerializer


@csrf_exempt
def api_echo(request):
    if request.method == 'GET':
        return HttpResponse("hello, {0}".format(request.user))
