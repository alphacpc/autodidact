from connectDB import conn, cursor;
from datas import data;

tab_matiere = [];

cursor.execute("""CREATE TABLE IF NOT EXISTS Matieres(
    nom_mat VARCHAR(25) NOT NULL PRIMARY KEY
)""");

##INSERT MATIERE ON TABLE MATIERES
for item in data:
    for el in item['Note']:
        if el['Matiere'].strip().startswith("A"):
            el['Matiere'] = "Anglais";
        
        if el['Matiere'].strip().startswith("F"):
            el['Matiere'] = "Francais";

        if el['Matiere'].strip() not in tab_matiere:
            tab_matiere.append(el['Matiere'].strip())
            cursor.execute("INSERT INTO Matieres(nom_mat) VALUES (%s)", (el['Matiere'].strip(),));

conn.commit();