from functools import wraps

def admin_image(image_field, width=None, height=None):
    def wrapped(s, obj):
        style = 'style="width: 10em;"'
        image = getattr(obj, image_field)
        if image:
            return u'<img src="%s" alt="%s" %s />' % (image.url, image.name, style)
        return u''
    wrapped.short_description = image_field
    wrapped.allow_tags = True
    return wrapped

def admin_color(field, colors):
    def wrapped(s, obj):
        v = getattr(obj, field, None)
        if v is not None:
            display = getattr(obj, 'get_%s_display' % field)()
            color = colors[v]
            return u'<span style="color: %s;">%s</span>' % (color, display)
        return u''
    wrapped.short_description = field
    wrapped.allow_tags = True
    return wrapped
