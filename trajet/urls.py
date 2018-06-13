from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'trajet'
urlpatterns = [
    path('trajets/', views.TrajetList.as_view(), name='trajet_list'),
    path('trajets/<int:pk>/', views.TrajetDetail.as_view(), name='trajet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
