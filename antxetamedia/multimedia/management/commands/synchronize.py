from django.core.management.base import BaseCommand

from antxetamedia.multimedia.models import Media
from antxetamedia.multimedia.handlers import upload


class Command(BaseCommand):
    help = 'Synchronize all Medias that are not'

    def handle(self, *args, **options):
        for media in Media.objects.order_by('-pk').filter(
                synchronize=True, is_synchronized=False).iterator():
            if media.local:
                bucket = media.bucket_name
                for retry in range(1, 5):
                    print('\nSyncing {}...'.format(bucket))
                    try:
                        uri = upload(user=media.account.user,
                                    passwd=media.account.password,
                                    bucket=media.bucket_name,
                                    metadata=media.metadata,
                                    key=media.key_name,
                                    fd=media.local.file)
                    except Exception, msg:
                        print('Failed: {}'.format(msg))
                    else:
                        if uri:
                            media.is_synchronized = True
                            media.remote = uri
                            media.save()
                            print('OK')
                            continue
                        print('Failed')
                    bucket = '{}-{}'.format(bucket, retry)
