from rest_framework import serializers
from trajet.models import Trajet, Mesure

class MesureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mesure
        fields = ('count', 'timestamp', 'latitude', 'longitude', 'speed', 'rpm', 'maf', 'load', 'acceleration', 'lacet', 'vitesse_limite' )


class TrajetSerializer(serializers.ModelSerializer):
    mesures = MesureSerializer(many=True, read_only=True)

    class Meta:
        model = Trajet
        fields = ('debut', 'duree', 'distance', 'note_eco', 'note_secu', 'note_conf', 'note_vit', 'note_glob', 'mesures' )
