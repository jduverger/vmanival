from django import template
register = template.Library()

@register.filter
def murl(own,url):
        return "/"+own+url
