from connectDB import conn, cursor;
from datas import data;

tab_matiere = [];

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    numero VARCHAR(7) PRIMARY KEY NOT NULL,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    date_naissance DATE NOT NULL,
    nom_classe VARCHAR(25) NOT NULL,
    FOREIGN KEY (nom_classe) REFERENCES Classes(nom_classe)
)""");


#INSERT STUDENT ON TABLE STUDENTS
for student in data:
    
    student["Date de naissance"] = student["Date de naissance"].split("/")[2]+"."+student["Date de naissance"].split("/")[1]+"."+student["Date de naissance"].split("/")[0]

    tup = (student['Numero'],student['Nom'],student['Prénom'],student["Date de naissance"],student['Classe'])

    cursor.execute("INSERT INTO Students(numero, nom, prenom, date_naissance, nom_classe) VALUES (%s,%s,%s,%s,%s)", tup);


conn.commit();