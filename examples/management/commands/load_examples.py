from django.core.management.base import BaseCommand
from examples.models import Example


class Command(BaseCommand):

    help = 'Load examples from find-similar to database'

    def handle(self, *args, **options):
        print('Load examples from find-similar package...')
        Example.load_from_find_similar()
        self.stdout.write(
            self.style.SUCCESS('All examples have been loaded')
        )
