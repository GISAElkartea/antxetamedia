from django.views.generic import TemplateView

from antxetamedia.misc.models import AboutUs


class AboutUsView(TemplateView):
    template_name = 'aboutus/aboutus.html'

    def get_context_data(self, **kwargs):
        c = super(AboutUsView, self).get_context_data(**kwargs)
        try:
            c['object'] = AboutUs.objects.all()[0]
        except IndexError:
            pass
        return c
