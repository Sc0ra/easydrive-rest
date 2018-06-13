from rest_framework import serializers
from django.contrib.auth.models import User
from easysensor.models import EasySensor
from easysensor.serializers import EasySensorSerializer

class UserSerializer(serializers.ModelSerializer):
    easysensors = EasySensorSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'easysensors')
