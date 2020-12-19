from django import template
register = template.Library()


@register.filter
def length(d):
    return len(d)
