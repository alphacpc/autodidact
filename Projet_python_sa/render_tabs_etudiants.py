import csv

Tab = [];
fieldnames = [];

def return_tabs(filename):    
    

    with open(filename) as csv_file:

        content = csv.reader(csv_file);
        fieldnames = [];
        Tab = [];
        count = 0;



        for row in content:
            
            # if count == 1:
            #     fieldnames = row
            
            # elif count > 2:
            #     dictionnaire = dict(zip(fieldnames,row))
            #     Tab.append(dictionnaire);

            # count += 1

            # if count >= 10:
            #     csv_file.close();   
            
            #     return Tab;

            if count < 10:
                if count == 1:
                    fieldnames = row
                    
                elif count >= 2:
                    dictionnaire = dict(zip(fieldnames,row))
                    Tab.append(dictionnaire);  

            count += 1  
            
        return Tab;