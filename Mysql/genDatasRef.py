from connecToDB import cursor,conn;
import random;

#DEFINE VAR
i = 1;
prix = 1000000;

#LOOP FOR INSERT DATAS TO REF TABLE
while i < 10 :
    
    key = round(random.random()* 10**4);
    
    cursor.execute("INSERT INTO reference(prix) VALUES(%s)", (prix*i + 500000,));
    
    i+=1;

conn.commit();