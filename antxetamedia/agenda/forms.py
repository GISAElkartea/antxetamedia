from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from uni_form.helpers import FormHelper, Submit, Layout, Fieldset
from uni_form import helpers

from antxetamedia.agenda.models import Happening


class HappeningForm(forms.ModelForm):
    class Meta:
        model = Happening

    @property
    def helper(self):
        helper = FormHelper()
        helper.add_input(Submit('submit', _('Submit!')))

        layout = Layout(
                Fieldset('', 
                    'name', 'description'),
                Fieldset(_('When and where'),
                    'date', 'time',
                    'town', 'other_town',
                    'place',
                    ),
                Fieldset(_('Details'),
                    'organizer', 'link', 'contact', 'image',
                    ),
                )

        helper.add_layout(layout)
        helper.form_action = reverse('agenda:create')
        helper.form_method = 'post'
        helper.form_style = 'inline'
        return helper
