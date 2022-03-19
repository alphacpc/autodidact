from connnectDB import conn, cursor
from tabulate import tabulate

reqs = [
    "SELECT adresse_AGENCE FROM AGENCE",
    "SELECT nom_USER FROM USERS WHERE id_PROFIL_PROFIL= 3 ORDER BY nom_USER",
    "SELECT nom_USER , adresse_AGENCE from USERS, AGENCE WHERE USERS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE AND id_PROFIL_PROFIL = 1",
    "SELECT numero_COMPTE_TRANSACTION, numero_AGENCE_AGENCE FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 4 ORDER BY montant_TRANSACTION",
    "MOUSSA DIOP",
    "SELECT nom_USER, numero_AGENCE_AGENCE FROM USERS WHERE numero_AGENCE_AGENCE = 2 AND id_PROFIL_PROFIL = 4",
    "SELECT Tab.numero_AGENCE,count(Tab.numero_AGENCE) as occurence FROM (SELECT TRANSACTIONS.numero_COMPTE_TRANSACTION, AGENCE.numero_AGENCE FROM `TRANSACTIONS`,  `AGENCE` WHERE TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE ORDER BY AGENCE.numero_AGENCE) as Tab GROUP BY Tab.numero_AGENCE",
    "SELECT date_debut, date_fin, numero_COMPTE_TRANSACTION FROM `ASSOCIER` WHERE id_USER_USER = 5 AND date_debut >= '2021-05-01' AND date_fin <= '2021-05-31'",
    "SELECT id_USER_USER, numero_COMPTE_TRANSACTION FROM `ASSOCIER` WHERE numero_COMPTE_TRANSACTION = 001 AND date_debut >= '2021-01-01' AND date_fin <= '2121-12-31'",
    "SELECT montant_TRANSACTION, id_USER_USER, date_TRANSACTION FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 001",
    "SELECT ASSOCIER.date_debut, ASSOCIER.date_fin, ASSOCIER.numero_COMPTE_TRANSACTION, USERS.nom_USER , USERS.numero_AGENCE_AGENCE FROM `ASSOCIER`, `USERS` WHERE ( ASSOCIER.date_debut >= '2021-01-01' AND ASSOCIER.date_fin <= '2021-04-30') AND ASSOCIER.id_USER_USER = USERS.id_USER AND USERS.numero_AGENCE_AGENCE = 001",
    "SELECT num_TRANSACTION, montant_TRANSACTION, date_TRANSACTION, numero_COMPTE_TRANSACTION, numero_AGENCE_AGENCE, id_TYPE_TYPE FROM `TRANSACTIONS` WHERE TRANSACTIONS.numero_AGENCE_AGENCE = 7 ORDER BY montant_TRANSACTION",
    "SELECT TRANSACTIONS.montant_TRANSACTION, TRANSACTIONS.frais_TRANSACTION FROM `TRANSACTIONS`, `USERS` WHERE USERS.numero_AGENCE_AGENCE = TRANSACTIONS.numero_AGENCE_AGENCE AND USERS.nom_USER = 'Assane Faye'",
    "SELECT * FROM (SELECT date_TRANSACTION, frais_TRANSACTION, id_TYPE_TYPE FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 001) as Tab, (SELECT * FROM PART WHERE libelle_PART != 'Systeme') as Par",
    "SELECT * FROM (SELECT date_TRANSACTION, frais_TRANSACTION, id_TYPE_TYPE FROM `TRANSACTIONS`) as Tab, (SELECT * FROM PART WHERE libelle_PART != 'Systeme') as Par WHERE Tab.date_TRANSACTION >= '2021-06-01' AND Tab.date_TRANSACTION <= '2021-12-31'"
]

def querySQL():
    cursor.execute("""SELECT * FROM (SELECT date_TRANSACTION, frais_TRANSACTION, id_TYPE_TYPE FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 001) as Tab, (SELECT * FROM PART WHERE libelle_PART != 'Systeme') as Par""")
    result =  cursor.fetchall();
    print(tabulate(result, headers=['Date', 'Frais', 'Type', 'id_PART','libelle_PART','Pourcentage'], tablefmt='psql'))

querySQL();

# def getAllAgence():
#     cursor.execute("""SELECT adresse_AGENCE FROM AGENCE""")
#     result =  cursor.fetchall();
#     print(tabulate(result, headers=['Adresse des Agence'], tablefmt='psql'))

#SELECT * FROM USERS WHERE nom_USER = "moussa diop" chef de l'agence 7;


#SELECT * FROM AGENCE WHERE adresse_AGENCE = "9 Banding Plaza";
