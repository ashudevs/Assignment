from rest_framework import serializers

from .models import *

class userdbserializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'