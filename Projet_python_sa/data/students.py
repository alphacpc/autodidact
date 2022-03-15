from connectDB import conn, cursor;
from datas import data;

tab_matiere = [];

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    numero VARCHAR(7) PRIMARY KEY NOT NULL,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    date_naissance DATE NOT NULL,
    id_classe INT NOT NULL,
    FOREIGN KEY (id_classe) REFERENCES Classes(id_classe)
)""");


#RECUP ALL DATA FROM CLASSES
tab = []
cursor.execute("SELECT * FROM Classes");
for k in cursor:

    tab.append(k)

#INSERT STUDENT ON TABLE STUDENTS
for student in data:
    
    student["Date de naissance"] = student["Date de naissance"].split("/")[2]+"."+student["Date de naissance"].split("/")[1]+"."+student["Date de naissance"].split("/")[0]

    for element in tab:
    
        if element[1] == student['Classe']:
            id_classe = element[0]

    tup = (student['Numero'],student['Nom'],student['Prénom'],student["Date de naissance"],id_classe)

    cursor.execute("INSERT INTO Students(numero, nom, prenom, date_naissance, id_classe) VALUES (%s,%s,%s,%s,%s)", tup);

for element in tab:

    if element[1] == data[34]['Classe']:
        print(data[34])
        print(data[34]['Classe'])
        id_classe = element[0]

print(id_classe);

conn.commit();