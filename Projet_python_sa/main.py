import render_tabs_etudiants;
import separate_valid_not_rows as terminator;
import module_fonctions as fonctions;

all_students = render_tabs_etudiants.return_tabs("datas.csv");

tab_valid, tab_invalid = terminator.separate_students_with_tab(all_students);

def stats():
    print("\nSur",len(all_students),"enregistrements on a :");
    print("\t",len(tab_valid),"informations valides, soit",round((len(tab_valid)*100)/len(all_students),2),"% des données.")
    print("\t",len(tab_invalid),"informations invalides, soit",round((len(tab_invalid)*100)/len(all_students),2),"% des données.")

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
    element = fonctions.get_element_by_numero('40DKG6T',all_students)
    print("\n*********Eleve : **********")
    for key in element:

        if key == 'Note':
            print("Note :")
            for item in element[key]:
                print("\t",item,"\n")
        else:

            print(key," : ",element[key])

    print("****************************")
        


elif int(xEntre) == 5:
    print('get les 5 premier')


elif int(xEntre) == 6:
    stats();

print('\n')
