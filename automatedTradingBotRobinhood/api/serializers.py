from rest_framework import serializers
from .models import LoginModel

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ('email', 'password')