import re
import datetime

# Checking column Date
def check_mounth(mounth):

    mounth_keys = [
        {"label":"ja","value":"01"},
        {"label":"f","value":"02"},
        {"label":"mar","value":"03"},
        {"label":"av","value":"04"},
        {"label":"mai","value":"05"},
        {"label":"juin","value":"06"},
        {"label":"juil","value":"07"},
        {"label":"ao","value":"08"},
        {"label":"sep","value":"09"},
        {"label":"o","value":"10"},
        {"label":"no","value":"11"},
        {"label":"d","value":"12"}
    ]

    for item in mounth_keys:
        if mounth.lower().startswith(item["label"]):
            mounth = item["value"]
            break
            
    return mounth


def check_date(born):

    seg = re.split('[-., _;:/ ]',born);

    if len(seg) > 3:
        return False

    else:
        seg[1] = check_mounth(seg[1]);
        
        if int(seg[2]) < 100:
            seg[2] = '19'+str(seg[2])

        try:
            datetime.datetime(int(seg[2]),int(seg[1]),int(seg[0]))
                
            return True;

        except ValueError:
                
            return False     
    
valeur = check_date("03/13/2001");

print("Hello", valeur)