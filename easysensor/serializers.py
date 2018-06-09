from rest_framework import serializers
from easysensor.models import EasySensor

class EasySensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasySensor
        fields = ('id', 'nom', 'device_id', 'user', 'activated' )
