from django.core.management.base import BaseCommand

from antxetamedia.multimedia.models import Media
from antxetamedia.multimedia.handlers import upload


class Command(BaseCommand):
    help = 'Synchronize all Medias that are not'

    def handle(self, *args, **options):
        for media in Media.objects.order_by('-pk').filter(
                synchronize=True, is_synchronized=False).iterator():
            if media.local:
                print 'Syncing {0}...'.format(media.related_object or media),
                try:
                    uri = upload(user=media.account.user,
                                 passwd=media.account.password,
                                 bucket=media.bucket_name,
                                 metadata=media.metadata,
                                 key=media.key_name,
                                 fd=media.local.file)
                    if uri:
                        media.is_synchronized = True
                        media.remote = uri
                    else:
                        media.is_synchronized = False
                except Exception, msg:
                    print 'Failed: {0}'.format(msg)
                else:
                    if media.is_synchronized:
                        print 'OK'
                    else:
                        print 'Failed'
                    media.save()
