import csv

count = 0;
Tab = [];

with open("Projet_datas.csv", newline='') as csv_file:

    content = csv.reader(csv_file);
    fieldnames = ["Code","Numero", "Nom", "Prenom", "Naissance", "Classe", "Note"];

    for row in content:
    
        if count > 2:
            # print(row)
            dictionnaire = dict(zip(fieldnames,row))
            # print(dictionnaire)
            Tab.append(dictionnaire);

        count += 1

        if(count >= 6): 
            break;

    print(Tab)
    print(len(Tab))
    print(Tab[2])
    # print(fieldnames);

    csv_file.close();