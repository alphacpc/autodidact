import math


label_notes = ["Matiere","Devoirs","Composition","moyenne"];


def notes_training(notes):
    
    tab_notes = [];
    


    if notes[0].startswith("#"):
        notes = notes[1:]
        
    

    separate_notes = notes.split("#")


    for notes in separate_notes:


        notes = notes.replace(',',';')
        notes = notes.rstrip();
        notes = notes.replace("]","");

        tab_matiere_note = notes.split("[")

        if(len(notes) == 0):
            tab_notes.append(dict(zip(label_notes, [0,0,0,0])))

        else: 
            moyenne = 0;
            moyenne_dev = 0;
            sum_dev = 0;
            
            try :

                # tab_matiere_note[1].split(":")[1]
                devoirs = tab_matiere_note[1].split(":")[0].split(';');
                compo = tab_matiere_note[1].split(":")[1]

                for dev in devoirs:
                    sum_dev += int(dev);
                
                moyenne_dev = sum_dev/len(devoirs);

                # print("La moyenne des devoirs ",tab_matiere_note[0],":",moyenne_dev,"\n")
                
                moyenne =  round((moyenne_dev + (2*int(compo)))/3, 2)


                tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),tab_matiere_note[1].split(":")[1],moyenne]

                tab_notes.append(dict(zip(label_notes, tableau_mat_dev_com)))


            except IndexError:
                tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),0,0]
                
                tab_notes.append(dict(zip(label_notes, tableau_mat_dev_com)));

    return tab_notes;
