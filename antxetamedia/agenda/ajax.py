from django.utils import simplejson
from django.core.urlresolvers import reverse

from dajaxice.core import dajaxice_functions
from datetime import date
today = date.today()

from antxetamedia.agenda.models import Happening


def happenings_for_month(request, year=today.year, month=today.month):
    dates = Happening.objects.filter(
            date__year=year,
            date__month=month,
            ).values_list('date')

    response = {}
    for date in dates:
        date = date[0]
        response[date.day] = reverse('agenda:day', args=(
            date.year, date.month, date.day))
    return simplejson.dumps(response)
dajaxice_functions.register(happenings_for_month)
