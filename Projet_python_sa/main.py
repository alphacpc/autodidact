import render_tabs_etudiants;
import separate_valid_not_rows as terminator;
import module_fonctions as fonctions;

all_students = render_tabs_etudiants.return_tabs("datas.csv");

tab_valid, tab_invalid = terminator.separate_students_with_tab(all_students);


fonctions.welcome();

xEntre = input("Donner: ");


while int(xEntre) < 1 or int(xEntre) > 6:
    xEntre = input("Donner un entier compris de 1 à 6 : ")


if int(xEntre) == 1:
    fonctions.get_all_elements_tabs(all_students,"Toutes les informations");


elif int(xEntre) == 2:
    fonctions.get_all_elements_tabs(tab_valid, "Les informations valides")
        

elif int(xEntre) == 3:
    fonctions.get_all_elements_tabs(tab_invalid, "Les informations invalides")
        

elif int(xEntre) == 4:
    xNumero = input("Donner un numéro composé de lettre majuscule, de chiffre et de longueur 7 : ")
    
    while not(len(xNumero)== 7 and xNumero.isupper() and xNumero.isalnum() and not xNumero.isalpha() and not xNumero.isdigit()):
        
        xNumero = input("Veuillez donner un numéro composé de lettre majuscule, de chiffre et de longueur 7 : ")

    fonctions.get_element_by_numero(xNumero,all_students)


elif int(xEntre) == 5:
    fonctions.top_five(tab_valid);


elif int(xEntre) == 6:
    fonctions.stats(all_students,tab_valid,tab_invalid);

