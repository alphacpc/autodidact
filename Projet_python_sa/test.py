import datetime;
import re

tab = ["12-jan.-87","21/10/1988","1-decembre-1993","05-01-1992","13 03-1994","18.2.1996"]
elements = [];

def switch_mounth(mounth):

    if mounth == "jan" or mounth == "Jan"  or mounth =="janvier" or mounth == "Janvier" or mounth=='1' or mounth =='01'  :
        return 1;
    elif mounth == "fév" or mounth =="février" or mounth=="fev" or mounth=="Fev" or mounth=='2' or mounth =='02':
        return 2;
    elif mounth == "mars" or mounth == "Mars" or mounth=='3' or mounth =='03':
        return 3;
    elif mounth == "avril" or mounth=="Avril" or mounth=='4' or mounth =='04':
        return 4;
    elif mounth == "mai" or mounth=="Mai" or mounth=='5' or mounth =='05':
        return 5;
    elif mounth == "juin" or mounth=="Juin" or mounth=='6' or mounth =='06':
        return 6;
    elif mounth == "juillet" or mounth=="Juillet" or mounth=='7' or mounth =='07':
        return 7;
    elif mounth == "aout" or mounth=="Aout" or mounth=='8' or mounth=="Aug" or mounth =='08':
        return 8;
    elif mounth == "sept" or mounth=="Sep" or mounth=="septembre" or mounth=="Septembre" or mounth=='9' or mounth =='09':
        return 9;
    elif mounth == "octobre" or mounth=="oct" or mounth=="Oct" or mounth=="Octobre" or mounth=='10' :
        return 10;
    elif mounth == "novembre" or mounth =="nov" or mounth =="Novembre" or mounth=='11':
        return 11;
    elif mounth == "décembre" or mounth == "decembre" or mounth == "dec" or mounth=="Dec" or mounth=="Decembre" or mounth=="Décembre" or mounth=='12' :
        return 12;
    else:
        return 0;


for item in tab:
    print(item)
    seg = re.split('[-./ ]',item);

    if len(seg) > 3:
        seg[1] = switch_mounth(seg[1]);
        

    else:
        seg[1] = str(switch_mounth(seg[1]));
        print(seg);
        elements.append(seg);
    print("\n")

#element = elements[0]
#print(element)
#print(datetime.datetime(int(element[2]),int(element[1]),int(element[0])).strftime("%d/%m/%Y"));

print(elements)

for element in elements:
    print(datetime.datetime(int(element[2]),int(element[1]),int(element[0])).strftime("%d/%m/%Y"));