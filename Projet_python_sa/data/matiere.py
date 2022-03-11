from connectDB import conn, cursor;

cursor.execute("""CREATE TABLE IF NOT EXISTS Matieres(
    nom_mat VARCHAR(25) NOT NULL PRIMARY KEY
)""");


conn.commit();