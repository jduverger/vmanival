from django import template
register = template.Library()

@register.filter
def decr(val):
    val=val-1
    if val < 1:
        return 1
    else:
        return val
    