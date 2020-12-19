from django import template
register = template.Library()


@register.filter
def index(d, i):
    return d[i]
