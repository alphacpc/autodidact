label_notes = ["Matiere","Devoirs","Composition"];


def notes_training(notes):
    
    tab_notes = []


    if notes[0].startswith("#"):
        notes = notes[1:]
        
    

    separate_notes = notes.split("#")


    for notes in separate_notes:


        notes.replace(',',';')
        notes = notes.rstrip();
        notes = notes.replace("]","");

        tab_matiere_note = notes.split("[")
        # print(tab_matiere_note)

        if(len(notes) == 0):
            tab_notes.append(dict(zip(label_notes, [0,0,0])))

        else: 
            
            try :

                # tab_matiere_note[1].split(":")[1]

                tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),tab_matiere_note[1].split(":")[1]]

                tab_notes.append(dict(zip(label_notes, tableau_mat_dev_com)))


            except IndexError:
                print("************Hello********")
                tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),0]
                
                tab_notes.append(dict(zip(label_notes, tableau_mat_dev_com)));

    return tab_notes;





print(notes_training("#HG[12:11] #SVT[12;10:8]  #Francais[14;11:4]  #PC[10;4:9] #Math[18:19]  #Anglais[4;8:16]"))
print("\n")
print(notes_training("Math[11;10;09:11] #PC[11;11;9:11]  #Francais[18;19;19:17]  #SVT[01:11] #HG[19:19]  #Anglais[19;17:19]"))
print("\n")
print(notes_training("#SVT[12:11] #PC[12:11]  #Anglais[15;14:12]  #Math[13:13] #HG[12:14]  #Francais[14,11:14]"))



#HG[12:11] #SVT[12;10:8]  #Francais[14;11:4]  #PC[10;4:9] #Math[18:19]  #Anglais[4;8:16]