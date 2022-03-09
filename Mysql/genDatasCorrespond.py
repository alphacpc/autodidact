from connecToDB import conn, cursor;
import random

#DEFINE VAR
i = 0;
tabs_pieces = [];
tabs_vehicules = []


#DEFINE FUNCTION FOR GET ALL ID FROM TABS (VEHICULE,PIECE)
def get_all_id_for_table(nametab):
    tabs =[]

    if nametab == "piece":
        cursor.execute("SELECT id_p FROM "+nametab);

    elif nametab == "vehicule":
        cursor.execute("SELECT id_veh FROM "+nametab);
    
    result = cursor.fetchall()

    for id in result:
        tabs.append(id[0])

    return tabs;

tabs_vehicules = get_all_id_for_table('vehicule')
tabs_pieces = get_all_id_for_table('piece')


#INSERT ELEMENT FOR CORRESPONDANCE
while i < 4:

    id_p = random.choice(tabs_pieces);
    id_v = random.choice(tabs_vehicules);
    mytuple = (id_p,id_v);

    cursor.execute("INSERT INTO correspondance(id_p, id_veh) VALUES(%s,%s)", (mytuple));

    i += 1;

conn.commit();