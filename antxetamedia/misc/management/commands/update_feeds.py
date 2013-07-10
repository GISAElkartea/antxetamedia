from django.core.management.base import BaseCommand

from sys import stdout

from misc.models import Feed


class Command(BaseCommand):
    args = 'None'
    help = 'Update all the feeds'

    def handle(self, *args, **kwargs):
        for feed in Feed.objects.all():
            stdout.write('Updating %s feed...' % feed.name)
            feed.update()
            stdout.write('OK\n')
