import render_tabs_etudiants;
import separate_valid_not_rows;
import re

arrray_students = render_tabs_etudiants.return_tabs("Projet_datas.csv");

tab_valid, tab_invalid =  separate_valid_not_rows.separate_rows(arrray_students);

#print("Sur",len(arrray_students),"enregistrements on a :");
#print("\tTaux d'enregistrement valide est :", round(len(tab_valid)*100/len(arrray_students),2),"%");
#print("\tTaux d'enregistrement invalide est :", round(len(tab_invalid)*100/len(arrray_students),2),"%");
n = 4

notes = arrray_students[15]['Note'].split("#");
print(arrray_students[n]['Note'])
print(notes)
notes[n] = notes[n].rstrip()
notes[n] = notes[n].replace("]","")

# print(notes[0][len(notes[0])-1])
print(notes[n])

mn= notes[n].split('[')
print(mn)
matiere = mn[0]
print(matiere)
note=mn[1].split(':')
print(note)
devoir= note[0].split(';')
composition=note[1]
print("devoir",devoir)
print("composition",composition)

moyenne=0;
sumDev=0
sumComp=0
for n in devoir:
    sumDev += int(n)
print("Somme des notes",sumDev);

print("Somme composition", int(composition))

moyenne = ((sumDev * (1/len(devoir)))+ 2*int(composition))/3
print("La moyenne vaut : ",round(moyenne,2));
