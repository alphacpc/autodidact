import docx

###############DECLARATION DES VARIABLES############
doc = docx.Document("Reqs.docx")
listMenuExec = []
listMenu = [p.text for p in doc.paragraphs]

###############DEFINITION DES FONCTIONS############
def showMenuG():
    ind = 1;
    for item in listMenu:
        print(ind, ":" ,item)
        ind += 1;
    print("\n")
    

def showMenuP():
    ind = 1;
    for item in listMenuExec:
        print(ind, ":" ,item)
        ind += 1;
    print("\n")

def showMenuMin():
    print("E ou e : Pour afficher les requêtes déjà choisi pour les réexécuter")
    print("R ou r : Pour réafficher tout le menu (exécuter ou non)")
    print("Q ou q : Pour quitter\n")


def checkChoice(enter):
    print(listMenu[int(enter) - 1])
    if listMenu[int(enter) - 1] not in listMenuExec:
        listMenuExec.append(listMenu[int(enter) - 1])



###############PROGRAMME PRINCIPALE############
showMenuG();

try:
    choix = int(input("\nVeuillez choisir une option : "))

    checkChoice(choix);
    
    xEntre = ""

    while xEntre != "q":

        showMenuMin()

        xEntre = input("Faites un autre choix : ").lower();
        
        if xEntre == "e":
            print("\nExecutés\n")
            showMenuP();

        elif xEntre == "r":
            print("\nRéafficher\n");
            showMenuG()
            choix = int(input("\nVeuillez choisir une option : "))
            checkChoice(choix);

        else:

            print("Porter votre choix entre (R, E, Q)")
        

except ValueError:
    print("Impossible de convertir cette chaine")
