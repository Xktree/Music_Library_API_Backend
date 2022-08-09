from django.http.response import Http404
from .models import Music 
from .serializers import MusicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 

# Create your views here.
