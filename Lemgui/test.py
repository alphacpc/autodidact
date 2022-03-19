from connnectDB import conn, cursor
from tabulate import tabulate

reqs = [
    "SELECT adresse_AGENCE FROM AGENCE",
    "SELECT nom_USER FROM USERS WHERE id_PROFIL_PROFIL= 3 ORDER BY nom_USER",
    "SELECT nom_USER , adresse_AGENCE from USERS, AGENCE WHERE USERS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE AND id_PROFIL_PROFIL = 1",
    "SELECT numero_COMPTE_TRANSACTION, numero_AGENCE_AGENCE FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 4 ORDER BY montant_TRANSACTION"
]

def querySQL():
    cursor.execute("""SELECT numero_COMPTE_TRANSACTION, numero_AGENCE_AGENCE FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 4 ORDER BY montant_TRANSACTION""")
    result =  cursor.fetchall();
    print(tabulate(result, headers=['Numero de Compte','Agence'], tablefmt='psql'))

querySQL();

# def getAllAgence():
#     cursor.execute("""SELECT adresse_AGENCE FROM AGENCE""")
#     result =  cursor.fetchall();
#     print(tabulate(result, headers=['Adresse des Agence'], tablefmt='psql'))



#SELECT * FROM AGENCE WHERE adresse_AGENCE = "9 Banding Plaza";
