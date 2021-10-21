from django.core.management.base import BaseCommand, CommandError
from shortenersite.models import Url
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Удаление ссылок старше 3 дней'

    def handle(self, *args, **options):
        Url.objects.filter(created_at__lte=datetime.now()-timedelta(days=3)).delete()
        self.stdout.write('Удалены ссылки старше 3 дней')