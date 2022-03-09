from connecToDB import cursor,conn;
import random;

#DEFINE VAR
i = 1;
prix = 1000000;

#LOOP FOR INSERT DATAS TO REF TABLE
while i < 10 :
    key = round(random.random()* 10**4);
    my_tuple = (key,prix * i+ 500000)
    cursor.execute("INSERT INTO reference(id_ref, prix) VALUES(%s, %s)", my_tuple);

    i+=1;
print("dialeu na")
conn.commit();