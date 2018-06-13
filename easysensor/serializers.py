from rest_framework import serializers
from easysensor.models import EasySensor
from trajet.models import Trajet
from trajet.serializers import TrajetSerializer

class EasySensorSerializer(serializers.ModelSerializer):
    trajets = TrajetSerializer(many=True, read_only=True)

    class Meta:
        model = EasySensor
        fields = ('id', 'nom', 'device_id', 'user', 'activated', 'trajets' )
