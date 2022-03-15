from connectDB import conn, cursor;
from datas import data;

tab_classes = [];

cursor.execute("""CREATE TABLE IF NOT EXISTS Classes(
    id_classe INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nom_classe VARCHAR(25) NOT NULL
)""");

##INSERT CLASSE NAME ON TABLE CLASSES
for item in data:
    if item["Classe"] not in tab_classes:
        tab_classes.append(item["Classe"]);
        cursor.execute("INSERT INTO Classes(nom_classe) VALUES (%s)", (item["Classe"],));

conn.commit();