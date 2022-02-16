import csv;
import functions.notes_dev_com as tr_notes;

Tab = [];

def return_tabs(filename):    
    
    fieldnames = [];
    count = 0;

    with open(filename) as csv_file:

        content = csv.reader(csv_file);
        
        for row in content:

            if count == 0:
                fieldnames = row[1:];
                    
            elif count >= 1:

                dictionnaire = dict(zip(fieldnames,row[1:]));

                Tab.append(dictionnaire);

            count += 1;
        
            
        return Tab;