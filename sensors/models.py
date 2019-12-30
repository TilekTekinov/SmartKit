from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    type = models.BigIntegerField()
    value = models.BigIntegerField()
    power = models.BooleanField()
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class SensorsLog(models.Model):
    sensor_id = models.BigIntegerField()
    date = models.DateTimeField()
    value = models.BigIntegerField()
