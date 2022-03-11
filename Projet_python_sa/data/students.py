from connectDB import conn, cursor;

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    numero VARCHAR(7) PRIMARY KEY NOT NULL,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    date_naissance DATE NOT NULL,
    nom_classe VARCHAR(25) NOT NULL,
    FOREIGN KEY (nom_classe) REFERENCES Classes(nom_classe)
)""");


conn.commit();