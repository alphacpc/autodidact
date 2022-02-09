label_notes = ["Matiere","Devoirs","Composition"];
tab_notes = []

def notes_training(notes):
    separate_notes = notes.split("#")


    for notes in separate_notes:

        notes.replace(',',';')
        notes = notes.rstrip();
        notes = notes.replace("]","");

        tab_matiere_note = notes.split("[")

        if(len(notes) == 0):
            tab_notes.append(dict(zip(label_notes, [0,0,0])))

        else: 
            
            try :
                tab_matiere_note[1].split(":")[1]

                tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),tab_matiere_note[1].split(":")[1]]

                tab_notes.append(dict(zip(label_notes, tableau_mat_dev_com)))


            except IndexError:

                tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),0]
                
                tab_notes.append(dict(zip(label_notes, tableau_mat_dev_com)));

    return tab_notes;





