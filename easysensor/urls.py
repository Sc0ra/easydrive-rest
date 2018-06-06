from django.urls import path, include

from . import views

app_name = 'easysensor'
urlpatterns = [
    path('', views.index, name='index'),
]
