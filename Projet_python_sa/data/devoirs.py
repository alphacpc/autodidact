from connectDB import conn, cursor;

cursor.execute("""CREATE TABLE IF NOT EXISTS Devoirs(
    id_dev INT NOT NULL AUTO_INCREMENT,
    dev1 INT NOT NULL,
    dev2 INT NOT NULL,
    dev3 INT NOT NULL,
    dev4 INT NOT NULL,
    dev5 INT NOT NULL,
    PRIMARY KEY (id_dev)
)""");


conn.commit();