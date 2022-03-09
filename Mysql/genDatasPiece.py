from connecToDB import conn, cursor;

#DEFINE VAR
tabs_refs = [];
tabs_category = ["Carosserie", "Mecanique","Electrique"]



#GET ALL 
cursor.execute("SELECT id_ref FROM  reference");
result = cursor.fetchall()
for ref in result:
    tabs_refs.append(ref[0]);


print(tabs_refs)

cursor.execute("INSERT INTO piece(categorie,date_recup,id_ref) VALUES(%s,%s,%s)", ("mecanique","12.11.2020",9684));
conn.commit();