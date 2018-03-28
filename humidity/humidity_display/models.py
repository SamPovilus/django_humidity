import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Humidity(models.Model):
    humidity = models.FloatField()
    temp = models.FloatField()
    log_date = models.DateTimeField('date logged')
    hostname = models.CharField(max_length=255)
    hostname.default = "dflt_humidity"
    def __str__(self):
        return "Humidity " + str(self.humidity)
    def was_logged_recently(self):
        return self.log_date >= timezone.now() - datetime.timedelta(days=1)

class Pressure(models.Model):
    pressure = models.FloatField()
    temp = models.FloatField()
    log_date = models.DateTimeField('date logged')
    hostname = models.CharField(max_length=255)
    hostname.default = "dflt_pressure"
    def __str__(self):
        return "Pressure " + str(self.pressure)
    def was_logged_recently(self):
        return self.log_date >= timezone.now() - datetime.timedelta(days=1)
