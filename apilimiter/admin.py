from django.contrib import admin
from .models import *


@admin.register(DailyLimits)
class DailyLimitsAdmin(admin.ModelAdmin):
    list_display = ['key', 'times']


@admin.register(HistoryLimits)
class HistoryLimitsAdmin(admin.ModelAdmin):
    list_display = ['key' , 'times' , 'date']


