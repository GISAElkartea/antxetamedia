from django.core.management.base import BaseCommand
from django.core.mail import mail_admins

from haystack import site

from multimedia.models import Media


class Command(BaseCommand):
    args = 'None'
    help = 'Synchronize all Medias that are not'

    def handle(self, *args, **kwargs):
        for media in Media.objects.order_by('-pk').filter(
                synchronize=True, is_synchronized=False).iterator():
            if media.local:
                print 'Syncing {0}...'.format(media.related_object or media),
                try:
                    media.sync()
                except Exception, msg:
                    print 'Failed: {0}'.format(msg)
                else:
                    if media.is_synchronized:
                        print 'OK'
                    else:
                        print 'Failed'
                    media.save()
