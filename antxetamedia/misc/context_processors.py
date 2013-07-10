from misc.models import Feed, Banner, HEADLINE

def headlines(request):
    return {'headlines': Feed.objects.filter(where=HEADLINE)}

def banner(request):
    try:
        return {'banner': Banner.objects.get(active=True)}
    except Banner.DoesNotExist:
        return {}
