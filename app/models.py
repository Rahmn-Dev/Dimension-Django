from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name