from typing import Any, List
from connecToDB import cursor,conn;
import random;

#DEFINE VAR
i = 1;
year = [2018, 2019, 2020, 2021, 2022];
marque = ["Rolls Royce", "Ford", "Chevrolet", "Dodge", "Jeep", "Lamborghini", "Porsche", "Tesla", "Mercedes-Benz"];
ended = ["X", "FX", "Y", "V4", "Z9", "B7"];

#FUNCTION FOR GENERATE MODELE FOR CARS
def generate_car_tuple(tabmark:List, tabyear:List, tabext:List):
    
    car_mark = random.choice(tabmark);
    car_year = random.choice(tabyear);
    car_ext = random.choice(tabext);

    car_modele = car_mark[0] + str(car_year) + car_ext;
        
    return (car_mark, car_year, car_modele);


while i < 20 :

    my_tuple = generate_car_tuple(marque, year, ended)

    cursor.execute("INSERT INTO vehicule(marque, annee, modele) VALUES(%s, %s, %s)", my_tuple);
    
    i+=1;

conn.commit();