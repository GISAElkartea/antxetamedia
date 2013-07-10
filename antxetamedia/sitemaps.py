from django.contrib.sitemaps import Sitemap, GenericSitemap

from recordings.models import News, Program
from agenda.models import Happening


news = {'queryset': News.objects.all(), 'date_field': 'pub_date'}
programs = {'queryset': Program.objects.all(), 'date_field': 'pub_date'}
happenings = {'queryset': Happening.objects.all(), 'date_field': 'date'}

statics = {
        'aboutus': {
            'location': '/about_us',
            'priority': .5,
            },
        'programazioa': {
            'location': '/programming',
            'priority': .6,
            }
        }

class StaticSitemap(Sitemap):
    def items(self):
        return statics.keys()
    def location(self, obj):
        return statics[obj]['location']
    def priority(self, obj):
        return statics[obj]['priority']


sitemaps = {
        'news': GenericSitemap(news, priority=1.0),
        'programs': GenericSitemap(programs, priority=0.9),
        'happenings': GenericSitemap(happenings, priority=0.8),
        'static': StaticSitemap(),
        }
