from django.views.generic import TemplateView

from multimedia.models import get_orphaned_media


class OrphanedMediaList(TemplateView):
    template_name = 'multimedia/video_list.html'

    def get_context_data(self, **kwargs):
        c = super(OrphanedMediaList, self).get_context_data(**kwargs)
        c['object_list'] = get_orphaned_media()
        return c
