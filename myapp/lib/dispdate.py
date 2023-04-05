def fdd(d):
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

def ddmmaaaa(d):
    vy=d[0:3]
    vm=d[4:5]
    vd=d[6:7]
    rd=vd+"/"+vm+"/"+vy
    return rd

def mmaaaa(d):
    vy=d[0:3]
    vm=d[4:5]
    vd=d[6:7]
    rd=vm+"/"+vy
    return rd
