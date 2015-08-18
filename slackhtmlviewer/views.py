from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET'])
def home(request):
    return render_to_response("index.html")