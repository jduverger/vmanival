def ylist(dates):
    tdate=dict()
    for fdate in dates:
        date = fdate[0:4]
        if date in tdate:
            tdate[date]+=1
        else:
            tdate[date]=1
    return tdate
