from django import template
register = template.Library()


@register.filter
def donn(d):
    return range(0,d)
