from rest_framework import serializers
from trajet.models import Trajet, Mesure

class TrajetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trajet
        fields = ('id', 'easysensor', 'debut', 'duree', 'distance', 'note_eco', 'note_secu', 'note_conf', 'note_vit', 'note_glob' )
