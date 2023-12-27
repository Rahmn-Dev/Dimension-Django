from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    price = models.FloatField()
    length = models.FloatField(null=True)
    width = models.FloatField(null=True)
    value = models.FloatField(null=True)
    def __str__(self):
        return self.name

class Container(models.Model):
    name = models.CharField(max_length=255)
    capacity_weight = models.FloatField(null=True)
    capacity_length = models.FloatField(null=True)
    capacity_width = models.FloatField(null=True)
    def __str__(self):
        return self.name
    
class Truck(models.Model):
    name = models.CharField(max_length=255)
    capacity_weight = models.FloatField(null=True)

    def __str__(self):
        return self.name