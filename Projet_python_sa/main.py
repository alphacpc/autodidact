import render_tabs_etudiants;
import separate_valid_not_rows;

arrray_students = render_tabs_etudiants.return_tabs("Projet_datas.csv");

tab_valid, tab_invalid =  separate_valid_not_rows.separate_rows(arrray_students);

print("***********TABLEAU VALID ************\n",tab_valid,"\n", len(tab_valid));
print("***********TABLEAU INVALID ************\n",tab_invalid,"\n", len(tab_invalid));
print("Longueur de notre numéro : ",len(arrray_students[0]["Numero"]));


