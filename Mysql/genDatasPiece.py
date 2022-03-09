from connecToDB import conn, cursor;
import time
import random

#DEFINE VAR
i = 0;
tabs_refs = [];
tabs_category = ["Carosserie", "Mecanique","Electrique"]


#GET ALL 
cursor.execute("SELECT id_ref FROM  reference");
result = cursor.fetchall()
for ref in result:
    tabs_refs.append(ref[0]);


print(tabs_refs)

while i < 20:

    #Generer des dates du 1-jan-2018 à la date actuel 
    #1515452400=1-jan-2018
    piece_date_recup = time.strftime('%d.%m.%Y', time.gmtime(random.randint(1515452400, int(time.time()))));

    piece_categ = random.choice(tabs_category);
    
    piece_ref = random.choice(tabs_refs)
   
    cursor.execute("INSERT INTO piece(categorie,date_recup,id_ref) VALUES(%s,%s,%s)", (piece_categ, piece_date_recup, piece_ref));

    i += 1;

conn.commit();