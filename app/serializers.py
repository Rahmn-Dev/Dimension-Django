from . import models
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = [
            "id",
            "name",
            "weight",
            "length",
            "width",
            "price",
            "value",
        ]
        
class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Container
        fields = [
            "id",
            "name",
            "capacity_weight",
            "capacity_length",
            "capacity_width",
        ]
        
class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Truck
        fields = [
            "id",
            "name",
            "capacity_weight",
        ]
        