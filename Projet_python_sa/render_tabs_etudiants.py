import csv;
import re;
import date_transform;

Tab = [];

def return_tabs(filename):    
    
    fieldnames = [];
    count = 0;

    with open(filename) as csv_file:

        content = csv.reader(csv_file);
        
        for row in content:

            if count < 220:
                if count == 1:
                    fieldnames = row;
                    
                elif count >= 2:
                    dictionnaire = dict(zip(fieldnames,row));
                    

                    # print(dictionnaire["Date de naissance"], "Dictionnaire date de naissance");
                    
                    # dictionnaire["Date de naissance"] = re.split('[-./ ]',dictionnaire["Date de naissance"]);
                    # dictionnaire["Date de naissance"] = date_transform.check_date_format("12/12/2002");
                    # print(date_transform.check_date_format(dictionnaire["Date de naissance"]), "Not valid")
                    dictionnaire["Date de naissance"] = date_transform.check_date_format(dictionnaire["Date de naissance"]);


                    Tab.append(dictionnaire);

            count += 1;
            
        return Tab;