from rest_framework import serializers
from django.contrib.auth.models import User
from easysensor.models import EasySensor

class UserSerializer(serializers.ModelSerializer):
    easysensors = serializers.PrimaryKeyRelatedField(many=True, queryset=EasySensor.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'easysensors')
