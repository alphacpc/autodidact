import datetime
import render_tabs_etudiants;
import separate_valid_not_rows;
from datetime import date

arrray_students = render_tabs_etudiants.return_tabs("Projet_datas.csv");

tab_valid, tab_invalid =  separate_valid_not_rows.separate_rows(arrray_students);

print("Sur",len(arrray_students),"enregistrements on a :");
print("\tTaux d'enregistrement valide est :", round(len(tab_valid)*100/len(arrray_students),2),"%");
print("\tTaux d'enregistrement invalide est :", round(len(tab_invalid)*100/len(arrray_students),2),"%");
print("Date de naissance de :", arrray_students[4]["Date de naissance"]);
print(datetime.datetime(arrray_students[4]["Date de naissance"]).strftime("%b %d %Y"))
print("Date de naissance de :", arrray_students[5]["Date de naissance"]);



# print("***********TABLEAU VALID ************\n",tab_valid,"\n", len(tab_valid));
# print("***********TABLEAU INVALID ************\n",tab_invalid,"\n", len(tab_invalid));
# print("Longueur de notre numéro : ",len(arrray_students[0]["Numero"]));


