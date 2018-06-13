from trajet.models import Trajet
from trajet.serializers import TrajetSerializer
from rest_framework import generics

class TrajetList(generics.ListCreateAPIView):
    queryset = Trajet.objects.all()
    serializer_class = TrajetSerializer

class TrajetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trajet.objects.all()
    serializer_class = TrajetSerializer
