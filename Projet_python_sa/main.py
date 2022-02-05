import csv
from itertools import count;

file = open("./Projet_datas.csv");
rows = csv.reader(file);
count= 0
for row in rows:
    print(row);
    # print(count)
    # count +=1


file.close();