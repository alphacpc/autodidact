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







def transform_date(born):

    seg = re.split('[-., _;:/ ]',born);

    return datetime.datetime(int(seg[2]),int(seg[1]),int(seg[0])).strftime("%d/%m/%Y"); 







# Checking Column classe level
def check_classe(level):

    level = level.replace(" ","");

    if ("em" in level) and len(level) == 4 and (level.endswith("A") or level.endswith("B")) and (level.startswith("6") or level.startswith("5") or level.startswith("4") or level.startswith("3")):
    
        return True;
    
    return False






#Checking notes
def check_notes(notes):
    
    if notes[0].startswith("#"):
        notes = notes[1:]
    
    separate_notes = notes.split("#")

    for notes in separate_notes:


        notes = notes.replace(',',';');
        notes = notes.rstrip();
        notes = notes.replace("]","");

        tab_matiere_note = notes.split("[");

        if(len(notes) == 0):
            return False;

        else: 

            if not(':' in tab_matiere_note[1]):
                return False;
            

            devoirs = tab_matiere_note[1].split(":")[0].split(';');

            compo = tab_matiere_note[1].split(":")[1]

            if(len(tab_matiere_note[1].split(":"))==12):
                return False

            for dev in devoirs:
                if int(dev)>20:
                    return False;

            if int(compo)>20:
                return False;


    return True;





def separate_students_with_tab(tabs):

    for row in tabs:
        
        sum_moyenne = 0;
        moyenne_g = 0;

        if (check_number(row["Numero"]) and 
            check_lname(row["Prénom"]) and 
            check_fname(row["Nom"]) and 
            check_classe(row["Classe"]) and
            check_date(row["Date de naissance"]) and
            check_field_empty(row) and
            check_notes(row["Note"])):
      
            row['Note'] = tr_notes.notes_training(row['Note'])

            for moyenne in row['Note']:
                sum_moyenne += int(moyenne['moyenne'])

            moyenne_g = round(sum_moyenne/6,2)
            row["Moyenne Generale"] = moyenne_g;
            row["Classe"] = row["Classe"].replace(" ", "");
            row["Date de naissance"] = transform_date(row["Date de naissance"])

            tab_valid.append(row);

        else:

            tab_invalid.append(row)
    
    return tab_valid,tab_invalid;

