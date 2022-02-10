import render_tabs_etudiants;
import separate_valid_not_rows as terminator;
import module_fonctions as fonctions;

all_students = render_tabs_etudiants.return_tabs("datas.csv");

tab_valid, tab_invalid = terminator.separate_students_with_tab(all_students);




fonctions.welcome();

xEntre = input("Donner: ")

while int(xEntre) > 1 and int(xEntre) > 6:
    xEntre = input("Donner valable: ")
    

if int(xEntre) == 1:
    fonctions.get_all_elements_tabs(all_students,"Toutes les informations");


elif int(xEntre) == 2:
    fonctions.get_all_elements_tabs(tab_valid, "Les informations valides")
    

elif int(xEntre) == 3:
    fonctions.get_all_elements_tabs(tab_invalid, "Les informations invalides")
    

elif int(xEntre) == 4:
    fonctions.get_element_by_numero('40DKG6T',all_students)


elif int(xEntre) == 5:
    print('get les 5 premier')


elif int(xEntre) == 6:
    fonctions.stats(all_students,tab_valid,tab_invalid);


