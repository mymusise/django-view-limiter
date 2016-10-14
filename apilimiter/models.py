from django.db import models


class DailyLimits(models.Model):
    key = models.CharField(max_length=128)
    times = models.IntegerField()

    class Meta:
        unique_together = ("id", "key")


class HistoryLimits(models.Model):
    key = models.CharField(max_length=128)
    times = models.IntegerField()
    date = models.DateField()
