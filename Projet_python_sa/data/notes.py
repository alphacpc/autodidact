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

# print(tab)


# for student in data:
#     num = student['Numero'];

#     for mat in student['Note']:


#         if mat["Matiere"].strip().startswith("A"):
#             mat["Matiere"] = "Anglais";
        
#         elif mat["Matiere"].strip().startswith("F"):
#             mat["Matiere"] = "Francais";

#         name = mat["Matiere"].strip()

#         for element in tab:
#             if element[1] == name:
#                 id_mat = element[0]

#         com = mat["Composition"];
#         devs = mat["Devoirs"]
#         print(devs, com, id_mat , num)

#         cursor.execute("INSERT INTO Evaluation VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", tu);




#conn.commit();



# print(data[4])
num = data[44]['Numero']
notes =  data[44]['Note']

# print(notes)
for student in data:

    num = student['Numero']
    notes =  student['Note']

    for note in notes:
        print(note['Matiere'],note['Devoirs'], note['Composition']);
        
        
        # print(note['Composition'],"comp",note['Matiere'],num )


        if note["Matiere"].strip().startswith("A"):
            note["Matiere"] = "Anglais";
            
        elif note["Matiere"].strip().startswith("F"):
            note["Matiere"] = "Francais";

        name = note["Matiere"].strip()

        for element in tab:
            if element[1] == name:
                id_mat = element[0]

        print(note['Composition'],2,note['Matiere'], id_mat,num )

        cursor.execute("INSERT INTO Notes(note_val, note_type, id_mat, numero) VALUES (%s, %s, %s, %s)", (int(note['Composition']),2, id_mat, num));

        for dev in note['Devoirs']:
            print(int(dev), 1 ,note['Matiere'], id_mat,num )

            cursor.execute("INSERT INTO Notes(note_val, note_type, id_mat, numero) VALUES (%s, %s, %s, %s)", (int(dev), 1 , id_mat ,num));


#cursor.execute("INSERT INTO Notes VALUES (%s, %s, %s, %s)", (12, type, svt, numero));

conn.commit();
