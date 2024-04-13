from rest_framework import serializers
from .models import Trader


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = ('username', 'password')