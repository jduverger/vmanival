from django import template
register = template.Library()

@register.filter
def addid(url,id):
        ids=str(id)
        return url+ids