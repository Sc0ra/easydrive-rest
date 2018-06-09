from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'easysensor'
urlpatterns = [
    path('easysensors/', views.EasySensorList.as_view(), name='easysensor_list'),
    path('easysensors/<int:pk>/', views.EasySensorDetail.as_view(), name='easysensor_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
