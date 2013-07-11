from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DayArchiveView, CreateView,\
        TemplateView

from datetime import date

from antxetamedia.agenda.forms import HappeningForm
from antxetamedia.agenda.models import Town, Happening


class BaseHappeningList(ListView):
    allow_empty=True

    def get_context_data(self, **kwargs):
        c = super(BaseHappeningList, self).get_context_data(**kwargs)
        c['towns'] = Town.objects.all()
        return c


class FutureHappeningList(BaseHappeningList):
    def get_queryset(self):
        return Happening.objects.future()


class TownHappeningList(BaseHappeningList):
    def get_queryset(self):
        self.town = get_object_or_404(Town, slug=self.kwargs['slug'])
        return Happening.objects.filter(town=self.town)

    def get_context_data(self, **kwargs):
        c = super(TownHappeningList, self).get_context_data(**kwargs)
        c['reason'] = self.town
        return c


class OtherTownHappeningList(TownHappeningList):
    def get_queryset(self):
        self.town = _('Other')
        return Happening.objects.filter(town__isnull=True,
                other_town__isnull=False)


class DayHappeningList(DayArchiveView):
    model = Happening
    date_field = 'date'
    template_name = 'agenda/happening_list.html'
    allow_future = True
    month_format = '%m'
            
    def get_context_data(self, **kwargs):
        c = super(DayHappeningList, self).get_context_data(**kwargs)
        c['towns'] = Town.objects.all()
        return c


class HappeningDetail(DetailView):
    model = Happening
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        c = super(HappeningDetail, self).get_context_data(**kwargs)
        c['towns'] = Town.objects.all()
        return c


class CreateHappening(CreateView):
    model = Happening
    form_class = HappeningForm

    def get_context_data(self, **kwargs):
        c = super(CreateHappening, self).get_context_data(**kwargs)
        c['towns'] = Town.objects.all()
        return c

class SuccessfulCreate(TemplateView):
    template_name = 'agenda/successful.html'
