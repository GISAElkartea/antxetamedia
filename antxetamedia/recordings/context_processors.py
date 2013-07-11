from antxetamedia.recordings.models import NewsCategory

def news_categories(request):
    return {'news_categories': NewsCategory.objects.all()}
