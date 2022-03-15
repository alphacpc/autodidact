from connectDB import conn, cursor;
from datas import data;


cursor.execute("""CREATE TABLE IF NOT EXISTS Evaluation(
    numero VARCHAR(7) NOT NULL,
    nom_mat VARCHAR(25) NOT NULL,
    comp INT NOT NULL,
    dev1 INT NOT NULL,
    dev2 INT NOT NULL,
    dev3 INT NOT NULL,
    dev4 INT NOT NULL,
    dev5 INT NOT NULL,
    PRIMARY KEY(numero, nom_mat)
)""");



#RECUP ALL DATA FROM CLASSES
tab = []
cursor.execute("SELECT * FROM Matieres");
for k in cursor:
    tab.append(k)



for student in data:
    num = student['Numero'];

    for mat in student['Note']:


        if mat["Matiere"].strip().startswith("A"):
            mat["Matiere"] = "Anglais";
        
        elif mat["Matiere"].strip().startswith("F"):
            mat["Matiere"] = "Francais";

        name = mat["Matiere"].strip()

        for element in tab:
            if element[1] == name:
                id_mat = element[0]

        com = mat["Composition"];
        devs = mat["Devoirs"]
        (dev1, dev2, dev3, dev4, dev5) = (0,0,0,0,0)

        for i in range(len(devs)):
    
            if (i==0):
                dev1 = int(devs[i]);
            elif (i==1):
                dev2 = int(devs[i]);
            elif (i==2):
                dev3 = int(devs[i]);
            elif (i==3):
                dev4 = int(devs[i]);
            elif (i==4):
                dev5 = int(devs[i]);
            else:
                continue;

        tu = (num, id_mat, int(com), dev1, dev2, dev3, dev4, dev5)

        cursor.execute("INSERT INTO Evaluation VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", tu);

conn.commit();