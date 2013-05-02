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
                'recordings.models.News', 
                'recordings.models.NewsCategory',
                'recordings.models.Program',
                ),
        ))

        self.children.append(modules.ModelList(
            _('Multimedia'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'multimedia.models.EmbededMedia',
                'multimedia.models.Media',
                'multimedia.models.Account',)
            ))

        self.children.append(modules.ModelList(
            _('Agenda'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'agenda.models.Happening', 
                'agenda.models.Town',
                ),
            ))

        self.children.append(modules.ModelList(
            _('Structure'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'structure.models.Node',
                ),
            ))

        self.children.append(modules.ModelList(
            _('Programming'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'programming.models.Emission',
                'programming.models.Producer',
                'programming.models.Category',
                ),
            ))

        self.children.append(modules.ModelList(
            _('Others'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=(
                'misc.models.Feed',
                'misc.models.Widget',
                'misc.models.Link', 
                'misc.models.Banner',
                'misc.models.AboutUs',
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
                ['Unai Zalakain', 'http://www.unaizalakain.info/contact/', True],
                ['Iune Trecet', 'mailto:iunetrecet@gmail.com', True],
            )
        ))

        self.children.append(modules.LinkList(
            title=_('Help'),
            column=3,
            children=(
                ('Idazteko sintaxia', 'http://www.squarespace.com/display/ShowHelp?section=Markdown', True),
            ),
        ))

