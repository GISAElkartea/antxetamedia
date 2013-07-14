"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'antxeta.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.ModelList(
            _('Recordings'),
            column=1,
            collapsible=True,
            models=(
                'antxetamedia.recordings.models.News', 
                'antxetamedia.recordings.models.NewsCategory',
                'antxetamedia.recordings.models.Program',
                ),
        ))

        self.children.append(modules.ModelList(
            _('Multimedia'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'antxetamedia.multimedia.models.EmbededMedia',
                'antxetamedia.multimedia.models.Media',
                'antxetamedia.multimedia.models.Account',)
            ))

        self.children.append(modules.ModelList(
            _('Agenda'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'antxetamedia.agenda.models.Happening', 
                'antxetamedia.agenda.models.Town',
                ),
            ))

        self.children.append(modules.ModelList(
            _('Structure'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'antxetamedia.structure.models.Node',
                ),
            ))

        self.children.append(modules.ModelList(
            _('Programming'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'antxetamedia.programming.models.Emission',
                'antxetamedia.programming.models.Producer',
                'antxetamedia.programming.models.Category',
                ),
            ))

        self.children.append(modules.ModelList(
            _('Others'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'antxetamedia.misc.models.Feed',
                'antxetamedia.misc.models.Widget',
                'antxetamedia.misc.models.Link', 
                'antxetamedia.misc.models.Banner',
                'antxetamedia.misc.models.AboutUs',
                ),
        ))


        self.children.append(modules.ModelList(
            _('Administrator'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'django.contrib.auth.models.User',
                'django.contrib.auth.models.Group',
                'django.contrib.sites.models.Site',
                ),
            ))

        self.children.append(modules.RecentActions(
            title=_('Latest Actions'),
            column=2,
            limit=10,
        ))

        self.children.append(modules.LinkList(
            title=_('Contact'),
            column=3,
            children=(
                ['Unai Zalakain', 'mailto:unai@gisa-elkartea.org', True],
                ['Iune Trecet', 'mailto:iunetrecet@gisa-elkartea.org', True],
            )
        ))

        self.children.append(modules.LinkList(
            title=_('Help'),
            column=3,
            children=(
                ('Idazteko sintaxia', 'http://www.squarespace.com/display/ShowHelp?section=Markdown', True),
            ),
        ))

