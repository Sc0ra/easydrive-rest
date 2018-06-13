from easysensor.models import EasySensor
from easysensor.serializers import EasySensorSerializer
from rest_framework import generics

class EasySensorList(generics.ListCreateAPIView):
    queryset = EasySensor.objects.all()
    serializer_class = EasySensorSerializer

class EasySensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EasySensor.objects.all()
    serializer_class = EasySensorSerializer
