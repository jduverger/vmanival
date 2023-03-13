from datetime import datetime

def datim():
    today=datetime.now()
    return today.strftime("%Y%m%d-%H%M%S")
