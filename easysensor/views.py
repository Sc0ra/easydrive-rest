from easysensor.models import EasySensor
from easysensor.serializers import EasySensorSerializer
from rest_framework import generics, permissions
from easysensor.permissions import IsOwner

class EasySensorList(generics.ListCreateAPIView):
    queryset = EasySensor.objects.all()
    serializer_class = EasySensorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EasySensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EasySensor.objects.all()
    serializer_class = EasySensorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwner)
class EasySensorListByUser(generics.ListCreateAPIView):
    serializer_class = EasySensorSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return EasySensor.objects.filter(user__id=user_id)

class EasySensorListCurrentUser(generics.ListCreateAPIView):
    serializer_class = EasySensorSerializer

    def get_queryset(self):
        user = self.request.user
        return EasySensor.objects.filter(user=user)
