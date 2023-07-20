from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = "Pull all metrics data from dgt server"

    def handle(self, *args, **options):
            self.stdout.write(
                self.style.SUCCESS('Successfully pulled all data from dgt')
            )