from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.encoding import smart_str

from urllib2 import HTTPError, URLError
from haystack import site
from os.path import join
from sys import stdout

from multimedia.models import Media

BLIP_URL = 'http://blip.tv/file/get/'

class Command(BaseCommand):
    args = 'None'
    help = 'Move medias from blip.tv to archive.org'

    def handle(self, *args, **kwargs):
        for media in Media.objects.exclude(remote__contains='archive.org').order_by('pk')[1:].iterator():
            print '{0}'.format(smart_str(media.related_object))
            print '-----------------------'
            if not media.local:
                if not media.remote.startswith(BLIP_URL):
                    media.remote = join(BLIP_URL, media.remote)
                print 'Downloading from {0}...'.format(smart_str(media.remote)),
                try:
                    media.download()
                except (HTTPError, URLError):
                    print 'Failed'
                    continue
                print 'OK'
                media.save()
            print 'Uploading from {0}...'.format(smart_str(media.local.path)),
            try:
                media.sync()
            except:
                print 'Failed'
                continue
            print 'OK'
            media.save()
            print
