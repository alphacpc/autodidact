def get_all_elements_tabs(tabs,title):

    print('\n\n*************************************************************')
    print('*****************',title,'******************\n')

    for row in tabs:
        for key in row:
            print(key,":",row[key],'\n')
        print("--------------------------------------")









def get_element_by_numero(num,tabs):
    
    count=0

    for row in tabs:
        if row['Numero'] == num:
            count = 1
            print("\n--------------------------------")
            for key in row:
                if key == 'Note':
                    print("Note :")
                    for item in row[key]:
                        print("\t",item,"\n")
                else:

                    print(key," : ",row[key])

            print("------------------------------------")
        

    if(count==0):
        print("\nDésolé ce numéro ne correspond à aucun élève.\n")
        print("*******à très bientot !******")    










def stats(all,valid,invalid):
    print("\nSur",len(all),"enregistrements on a :\n");
    print("\t",len(valid),"informations valides, soit",round((len(valid)*100)/len(all),2),"% des données.\n")
    print("\t",len(invalid),"informations invalides, soit",round((len(invalid)*100)/len(all),2),"% des données.\n")










def by_moyenne(entry):
    return entry["Moyenne Generale"];


def top_five(tabs):

    count = 0


    tabs.sort(key=by_moyenne,reverse=True)

    for row in tabs:
        
        if count < 5:
            rang = count+1
            print("Range",rang," est : ",row,'\n')
        count +=1





def welcome():
    
    print('\n')
    print('*************************************************************')
    print('*****************BIENVENU AU PROJET PYTHON*******************')
    print('*************************************************************')


    print('1 : Pour afficher toutes les informations');
    print('2 : Pour afficher les informations valides');
    print('3 : Pour afficher les informations invalides');
    print('4 : Pour afficher une information (par son numéro)');
    print('5 : Pour afficher les cinq premiers informations');
    print('6 : Pour afficher les statistiques');


 