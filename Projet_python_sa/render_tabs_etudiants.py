import csv;

Tab = [];

def return_tabs(filename):    
    
    fieldnames = [];
    count = 0;

    with open(filename) as csv_file:

        content = csv.reader(csv_file);
        
        for row in content:

            if count < 10:
                if count == 1:
                    fieldnames = row;
                    
                elif count >= 2:
                    dictionnaire = dict(zip(fieldnames,row));
                    Tab.append(dictionnaire);  

            count += 1;
            
        return Tab;