from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from uni_form.helpers import FormHelper, Submit


class SearchForm(ModelSearchForm):
    from_date = forms.DateField(label=_('From'), required=False)
    to_date = forms.DateField(label=_('To'), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['q'].label = _('What?')
        self.fields['models'].label = _('Where?')

    def search(self):
        sqs = super(SearchForm, self).search()
        if self.is_valid():
            data = self.cleaned_data
            if any(data.values()):
                if data['from_date']:
                    sqs = sqs.filter(date__gte=data['from_date'])
                if data['to_date']:
                    sqs = sqs.filter(date__lt=data['to_date'])
                return sqs
        return EmptySearchQuerySet()


    def no_query_found(self):
        return SearchQuerySet()

    @property
    def helper(self):
        helper = FormHelper()
        helper.add_input(Submit('submit', _('Search')))
        
        helper.form_action = reverse('search:search')
        helper.form_method = 'get'
        return helper
