import csv;
import re

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
                    # print(dictionnaire,"\n")
                    # print(dictionnaire["Date de naissance"],"\n")
                    dictionnaire["Date de naissance"] = re.split('[-./ ]',dictionnaire["Date de naissance"]);
                    # print(seg,"\n")
                    Tab.append(dictionnaire);  

            count += 1;
            
        return Tab;