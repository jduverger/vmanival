def tlist(thems):
    tthema=dict()
    for thema in thems:
        if thema in tthema:
            tthema[thema]+=1
        else:
            tthema[thema]=1
    return tthema
