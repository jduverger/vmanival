from django import template
register = template.Library()

@register.filter
def dispddmy(d):
    vy=d[0:4]
    vm=d[4:6]
    vd=d[6:8]
    switcher = {
        "01":"janv",
        "02":"fevr",
        "03":"mars",
        "04":"avril",
        "05":"mai",
        "06":"juin",
        "07":"juill",
        "08":"aout",
        "09":"sept",
        "10":"oct",
        "11":"nov",
        "12":"dec"
        }
    dm=switcher.get(vm,"xxx")
    rd=vd+"/"+dm+"/"+vy
    return rd