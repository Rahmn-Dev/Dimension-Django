from rest_framework import viewsets, permissions

from . import serializers
from . import models
from django_filters import rest_framework as filters
from rest_framework.response import Response

class ItemApiViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    
class ContainerApiViewSet(viewsets.ModelViewSet):
    queryset = models.Container.objects.all()
    serializer_class = serializers.ContainerSerializer
    
class TruckApiViewSet(viewsets.ModelViewSet):
    queryset = models.Truck.objects.all()
    serializer_class = serializers.TruckSerializer