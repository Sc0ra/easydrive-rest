from django.db import models
from django.contrib.auth.models import User

class EasySensor(models.Model):
    nom = models.CharField(max_length=100)
    device_id = models.IntegerField()
    user = models.ForeignKey(User, related_name='easysensors', on_delete=models.CASCADE,null = True)
    activated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.nom)
