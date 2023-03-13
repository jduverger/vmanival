from PIL import Image

def attachref(orifname,w,h,fpath):
    bname=orifname.split(".")[0]
    ext=orifname.split(".")[1]
    maxdim=500
    OKlist=("jpg","JPG","jpeg","JPEG","gif","GIF","png","PNG")
    if ext in OKlist:
        if w > maxdim  or  h > maxdim :
            if w > h :
                h=str(int(h/(w/maxdim)))
                w=str(maxdim)
            else:
                w=str(int(w/(h/maxdim)))
                h=str(maxdim)
        code="<br><p align='center'><img src='"+fpath+"' width='"+w+"' height='"+h+"' title='' alt=''></p>"
    elif ext == "pdf":
        code="<br><p><a href='"+fpath+"' target='_blank'><img src='/static/icon_hand_r.png'>"+bname+"</a></p>"
    else:
        code="<br><p><a href='"+fpath+"'>X-"+bname+"</a></p>"
    return code
