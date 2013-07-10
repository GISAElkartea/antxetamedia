from haystack.views import SearchView as HSearchView

from search.forms import SearchForm


class SearchView(HSearchView):
    def __init__(self, *args, **kwargs):
        super(SearchView, self).__init__(*args, **kwargs)
        self.form_class = SearchForm
        self.results_per_page = 10
        self.template = 'search/search_list.html'
