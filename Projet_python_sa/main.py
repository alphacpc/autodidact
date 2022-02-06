import datetime
import render_tabs_etudiants;
import separate_valid_not_rows;
from datetime import date

arrray_students = render_tabs_etudiants.return_tabs("Projet_datas.csv");



tab_valid, tab_invalid =  separate_valid_not_rows.separate_rows(arrray_students);

print("Sur",len(arrray_students),"enregistrements on a :");
print("\tTaux d'enregistrement valide est :", round(len(tab_valid)*100/len(arrray_students),2),"%");
print("\tTaux d'enregistrement invalide est :", round(len(tab_invalid)*100/len(arrray_students),2),"%");

print(arrray_students[0])




