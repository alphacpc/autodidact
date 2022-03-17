from connectDB import conn, cursor;
from datas import data;


cursor.execute("""CREATE TABLE IF NOT EXISTS Notes(
    id_note INT AUTO_INCREMENT NOT NULL,
    note_val INT NOT NULL,
    note_type INT NOT NULL,
    id_mat INT NOT NULL,
    numero VARCHAR(7) NOT NULL,
    PRIMARY KEY(id_note,numero, id_mat)
)""");



#RECUP ALL DATA FROM CLASSES
tab = []
cursor.execute("SELECT * FROM Matieres");
for k in cursor:
    tab.append(k)



#ADDED DATA FOR TAB NOTES
for student in data:

    num = student['Numero']
    notes =  student['Note']

    for note in notes:

        if note["Matiere"].strip().startswith("A"):
            note["Matiere"] = "Anglais";
            
        elif note["Matiere"].strip().startswith("F"):
            note["Matiere"] = "Francais";

        name = note["Matiere"].strip()

        for element in tab:
            if element[1] == name:
                id_mat = element[0]

        cursor.execute("INSERT INTO Notes(note_val, note_type, id_mat, numero) VALUES (%s, %s, %s, %s)", (int(note['Composition']),2, id_mat, num));

        for dev in note['Devoirs']:

            cursor.execute("INSERT INTO Notes(note_val, note_type, id_mat, numero) VALUES (%s, %s, %s, %s)", (int(dev), 1 , id_mat ,num));

#conn.commit();