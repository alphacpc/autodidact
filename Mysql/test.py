import random;
i = 1;
prix = 1000000;
datas = []


while i < 10 :
    value = round(random.random()* 10**10);
    print(value, prix * i+ 500000)
    mydisc = {"identifiant": value, "prix": prix}
    datas.append(mydisc)
    i+=1;

print(datas)