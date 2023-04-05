import datetime

def gnorm(date):
    # months 0 to 11 on google timeline
    # when javascript notation used, i.e 2020,3,1
    # not when string used, i.e "2020,3,1" 
    return date

def datetodays(date):
    return days

def daystodate(days):
    return date

def stringtodate(mydate):
    year=int(mydate.split("-")[0])
    month=int(mydate.split("-")[1])
    days=int(mydate.split("-")[2])
    return datetime.date(year,month,days)

def datetostring(date):
    return str(date.year)+"-"+str(date.month)+"-"+str(date.day)

def adddays(mydate,nb):
    return mydate+datetime.timedelta(days=nb)

def diffdate(firstdate,secdate):
    return nbdays


