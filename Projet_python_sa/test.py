import datetime;
import re

tab = ["12-01-87","21/10/1988","1-2-1993","05-01-1992","13 03-1994","18.2.1996"]
elements = [];
tes = [];

for item in tab:
    print(item)
    # print(item.split())
    seg = re.split('[-./ ]',item);
    print(seg)
    for i in seg:
        int(i)

    elements.append(seg)
    print("\n")

element = elements[1]
print(element)
print(datetime.datetime(int(element[2]),int(element[1]),int(element[0])).strftime("%d/%m/%Y"));