import re
import datetime
import notes_dev_com as tr_notes;

tab_valid = [];
tab_invalid = [];



#Check field by field if empty()
def check_field_empty(row):
    
    for key in row:

        if len(row[key])==0:
            # print("Bakhoullll !!!")

            return False

    return True






# Checking column Numero
def check_number(column_number):

    if len(column_number)== 7 and column_number.isupper() and column_number.isalnum() and not column_number.isalpha() and not column_number.isdigit():
        return True
    
    return False




# Checking Column Firstname
def check_fname(fname):

    if len(fname) >= 3 and fname[0].isalpha() and fname.isalpha():
        return True
    
    return False;




# Checking Column Lastname
def check_lname(lname):

    if len(lname) >= 2 and lname[0].isalpha() and lname.isalpha():
        return True
    
    return False;





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
        
        if mounth.isalpha():

            if mounth.lower().startswith(item["label"]) or mounth.startswith(item["label"]):
                mounth = item["value"]
        else :
            mounth = mounth

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

    level = level.replace(" ","");

    if ("em" in level) and len(level) == 4 and (level.endswith("A") or level.endswith("B")) and (level.startswith("6") or level.startswith("5") or level.startswith("4") or level.startswith("3")):
    
        return True;
    
    return False





def separate_students_with_tab(tabs):

    for row in tabs:
        if (check_number(row["Numero"]) and 
            check_lname(row["Prénom"]) and 
            check_fname(row["Nom"]) and 
            check_classe(row["Classe"]) and
            check_date(row["Date de naissance"]) and
            check_field_empty(row)):
            
            # print(len(row),"\n")
            # print(row["Numero"])
            row['Note'] = tr_notes.notes_training(row['Note'])
            # print(row['Note'])
            tab_valid.append(row);

        else:

            tab_invalid.append(row)
    
    return tab_valid,tab_invalid;

