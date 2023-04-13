def tlist(thems):
    tthema=dict()
    for thema in thems:
        if thema in tthema:
            tthema[thema]+=1
        else:
            tthema[thema]=1
    thema_sorted_by_value=sorted(tthema.items(), key=lambda x:x[1], reverse=True)
    tthema=dict(thema_sorted_by_value)
    return tthema
