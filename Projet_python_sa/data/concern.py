from connectDB import conn, cursor;

cursor.execute("""CREATE TABLE IF NOT EXISTS Concerns(
    numero VARCHAR(7) NOT NULL,
    nom_mat VARCHAR(25) NOT NULL,
    id_dev INT NOT NULL,
    PRIMARY KEY (numero, nom_mat, id_dev)
)""");


conn.commit();