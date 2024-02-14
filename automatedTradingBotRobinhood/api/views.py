from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from models import Login
from serializers import LoginSerializer

# Create your views here.
class ModelView(APIView):
    pass

class BotView(APIView):
    pass

class LoginView(APIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

