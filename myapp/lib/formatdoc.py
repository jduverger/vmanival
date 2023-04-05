from PIL import Image

def attachref(orifname,fpath,pos_img):
    bname=orifname.split(".")[0]
    ext=orifname.split(".")[1]
    OKlist=("jpg","JPG","jpeg","JPEG","gif","GIF","png","PNG")
    if ext in OKlist:
        code="<img class='"+pos_img+"' src='"+fpath+"'>"
        if pos_img =="imgcenter":
            code="<div style='text-align:center;'>"+code+"</div>"
    elif ext == "pdf":
        code="<br><p><a href='"+fpath+"' target='_blank'><img src='/static/icon_hand_r.png'>"+bname+"</a></p>"
    else:
        code="<br><p><a href='"+fpath+"'>X-"+bname+"</a></p>"
    return code
