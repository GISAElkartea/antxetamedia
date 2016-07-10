from boto.s3.connection import S3Connection
from boto.s3.bucket import Bucket
from boto.exception import S3ResponseError, S3CreateError

from django.conf import settings


def upload(user, passwd, bucket, metadata, key, fd):
    conn = S3Connection(user, passwd, host=settings.S3_HOST, is_secure=False)

    while bucket.endswith('-'):
        bucket = bucket[:-1]
    try:
        bucket = conn.get_bucket(bucket)
    except S3ResponseError:
        try:
            bucket = conn.create_bucket(bucket, headers=metadata)
        except S3CreateError as e:
            if e.status == 409:
                bucket = Bucket(conn, bucket)

    key = bucket.new_key(key)
    try:
        key.set_contents_from_file(fd)
    except S3ResponseError:
        key.set_contents_from_file(fd)

    return key.generate_url(0).split('?')[0]
