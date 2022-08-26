from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    temp = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')