from django.core.management.base import BaseCommand
from apilimiter.models import DailyLimits, HistoryLimits
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        today = datetime.date.today()
        """
        delete the limit yestoday not use
        """
        DailyLimits.objects.filter(times=0).delete()
        daily_data = DailyLimits.objects.all()
        histories = [HistoryLimits(
            key=limit.key, times=limit.times, date=today
        ) for limit in daily_data]
        HistoryLimits.objects.bulk_create(histories)
        daily_data.update(times=0)
