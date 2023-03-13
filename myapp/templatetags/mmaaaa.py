from django import template
register = template.Library()

@register.filter
def mmaaaa(d):
    vy=d[0:4]
    vm=d[4:6]
    rd=vm+"/"+vy
    return rd
