from django.db import models
import time


class DailyLimits(models.Model):
    key = models.CharField(max_length=128)
    times = models.IntegerField()
    time_left = models.IntegerField(default=time.time())

    class Meta:
        unique_together = ("id", "key")


class HistoryLimits(models.Model):
    key = models.CharField(max_length=128)
    times = models.IntegerField()
    date = models.DateField()
