import csv;
import date_transform;

Tab = [];

def return_tabs(filename):    
    
    fieldnames = [];
    count = 0;

    with open(filename) as csv_file:

        content = csv.reader(csv_file);
        
        for row in content:

            if count < 222:
                if count == 1:
                    fieldnames = row;
                    
                elif count >= 2:
                    dictionnaire = dict(zip(fieldnames,row));
                    
                    try:
                        # dictionnaire["Date de naissance"] = date_transform.check_date_format(dictionnaire["Date de naissance"]);

                        Tab.append(dictionnaire);

                    except ValueError:
                        pass


            count += 1;
            
        return Tab;