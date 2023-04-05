def splittx(txcontent):
    listst=[]
    statementlist=txcontent.split('CREATE')
    for txitem in statementlist:
        if txitem != "":
            listst.append("CREATE"+txitem)
    return listst
    