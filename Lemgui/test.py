listMenuExec = []
listMenu = [
    "Lister les tous les agences",
    "Lister tous les caissiers par ordre croissant de leur nom",
    "Lister tous chef d’agence ainsi que le nom de l’agence",
    "Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
    "Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant",
    "Lister les utilisateurs de l’agence Plateau",
    "Lister le nombre de compte par agence",
    "Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
    "Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
    "Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001",
    "Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
    "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa diop par ordre croissant du montant",
    "Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop .",
    "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.",
    "Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
    "Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
    "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
    "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
    "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
    "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
    "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 221",
    "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
    "Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
    "Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
    "Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop",
]



def showMenuG():
    ind = 1;

    for item in listMenu:
        
        print(ind, ":" ,item)
        
        ind += 1;

def checkChoise(enter):

    print(listMenu[int(enter) - 1])

    if listMenu[int(enter) - 1] not in listMenuExec:
        
        listMenuExec.append(listMenu[int(enter) - 1])


showMenuG();

choices = input("\nVeuillez choisir une option : ")

checkChoise(choices)