def paintht(content):
	posdeb=content.find("#")
	if posdeb < 0 :
		return content
	posfin=content.find("</a>")
	ifin1=posdeb-1
	ifin2=posfin-1
	ideb=posfin+4
	strc=content[:ifin1]\
		+"<span style=\"color:blue\">"\
		+content[posdeb:ifin2]\
		+"</span>"\
		+content[ideb:]
	return strc

