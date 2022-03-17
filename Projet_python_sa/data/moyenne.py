from connectDB import conn, cursor;
from datas import data;


cursor.execute("""DROP TABLE IF EXISTS Moyennes""");

cursor.execute("""CREATE TABLE IF NOT EXISTS Moyennes(
    id_moy INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    moyenne INT NOT NULL,
    numero VARCHAR(7) NOT NULL,
    FOREIGN KEY (numero) REFERENCES Students(numero)
)""");

for student in data:
    num_st = student['Numero'];
    moy = student['Moyenne Generale'];
    

    cursor.execute("INSERT INTO Moyennes(moyenne, numero) VALUES (%s,%s)", (moy, num_st));



conn.commit()