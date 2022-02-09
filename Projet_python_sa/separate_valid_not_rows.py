import re
import datetime

tab_valid = [];
tab_invalid = [];



# Checking column Numero
def check_number(column_number):

    if (len(column_number) != 7) or column_number.islower()== True or column_number.isalnum()==False :
        return False
    
    return True




# Checking Column Firstname
def check_fname(fname):

    if len(fname) < 3 or fname[0].isalpha() == False:
        return False
        
    return True;







# Checking Column Lastname
def check_lname(lname):

    if len(lname) < 2 or lname[0].isalpha() == False:
        return False
        
    return True;





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
        {"label":"n","value":"11"},
        {"label":"d","value":"12"}
    ]

    for item in mounth_keys:
        if mounth.lower().startswith(item[0]):
            mounth = item["value"]
        
    return mounth;


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



# Checking Column classe level
def check_classe(level):

    if ("em" in level)==False and len(level) != 4 and (level.endswith("A")==False or level.endswith("B")==False):
        return False;
    
    return True





def separate_students_with_tab(tabs):

    for row in tabs:
        if check_number(row["Numero"]) or check_lname(row["Prénom"]) or check_fname(row["Nom"]) or check_classe(row["Classe"]) or check_date(row["Date de naissance"]):
            print("Baaaaaaakhoul !!!")
        else:
            print("Nice !!!")


