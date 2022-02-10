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
    fonctions.top_five(tab_valid);


elif int(xEntre) == 6:
    fonctions.stats(all_students,tab_valid,tab_invalid);



# tab = []
# for item in tab_valid:

#     matricule = str(item["Numero"]);
#     moyenne = str(item['Moyenne Generale'])

#     my_tuple = (matricule,moyenne)
#     tab.append(my_tuple)

# print(tab)


# print("\n")

# def order_de_merite(tup): 
    
#     tup.sort(key = lambda x: float(x[1]), reverse = True) 
#     print("salam",tup) 

# order_de_merite(tab)


# [1,4,9].sort()


# count = 0
# def by_moyenne(entry):
#     return entry["Moyenne Generale"];

# tab_valid.sort(key=by_moyenne,reverse=True)

# for row in tab_valid:
    
#     if count < 5:
#         rang = count+1
#         print("Range",rang," est : ",row,'\n')
#     count +=1


# for item in tab_valid:

#     matricule = str(item["Numero"]);
#     moyenne = item['Moyenne Generale']

#     tupl = (matricule,moyenne)
    
#     tab.append(moyenne)
# print("Non ordonné",tab)
# tab.sort(reverse=True)
# print("\n")
# print("Ordonné",tab)
# print("Premier",tab[0])
