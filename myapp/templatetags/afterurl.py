from django import template
register = template.Library()

@register.filter
def afterurl(bid,url):
        return url+"/"+bid
