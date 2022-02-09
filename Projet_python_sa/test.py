from operator import ne


label_notes = ["Matiere","Devoirs","Composition"];
newTab = []

def notes_training(notes):
    separate_notes = notes.split("#")
    print("Les notes :",separate_notes);

    for notes in separate_notes:

        notes = notes.rstrip();
        notes = notes.replace("]","");
        print(notes)

        tab_matiere_note = notes.split("[")
        # print(tab_matiere_note)
        # print("Matiere",tab_matiere_note[0])
        # print("Note",tab_matiere_note[1].split(":"))
        # print("Devoir",tab_matiere_note[1].split(":")[0].split(';'))
        # print("Composition",tab_matiere_note[1].split(":")[1])
        tableau_mat_dev_com = [tab_matiere_note[0],tab_matiere_note[1].split(":")[0].split(';'),tab_matiere_note[1].split(":")[1]]
        dic = dict(zip(label_notes, tableau_mat_dev_com))
        newTab.append(dic )
    return newTab

        # for element in tab_matiere_note:
        #     pass

        # label_matiere = tab_matiere_note[0];
        # items_notes = tab_matiere_note[1]
        # tab_dev_comp = items_notes.split(':');
        # tab_dev = tab_dev_comp[0].split(";")
        # tab_com = tab_dev_comp[1];
        # print(tab_matiere_note);
        # print("Matiere :",label_matiere);
        # print(items_notes)
        # print(tab_dev_comp)
        # print("Devoir : ",tab_dev);
        # print("Composition :",tab_com);
        # newTab = [label_matiere, tab_dev, tab_com]
        
        # my_dict = dict(zip(label_notes,newTab))

