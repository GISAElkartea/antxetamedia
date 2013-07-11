from django.utils.dates import WEEKDAYS_ABBR
from django.views.generic import TemplateView

from operator import itemgetter

from antxetamedia.programming.models import Space, Producer, Category

weekdays = WEEKDAYS_ABBR

class Programming(TemplateView):
    template_name = 'programming/programming.html'

    def get_context_data(self, **kwargs):
        c = super(Programming, self).get_context_data(**kwargs)

        table = {}
        for space in Space.objects.all():
            for piece in space.get_pieces():
                if not table.has_key(piece):
                    table[piece] = dict.fromkeys(weekdays.keys(), '')
                table[piece][space.weekday] = space

        c['spaces'] = sorted(table.items(), key=itemgetter(0))
        c['weekdays'] = weekdays.values()
        c['producers'] = Producer.objects.all()
        c['categories'] = Category.objects.all()
        return c
