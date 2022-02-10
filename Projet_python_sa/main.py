import render_tabs_etudiants;
import separate_valid_not_rows as terminator;



all_students = render_tabs_etudiants.return_tabs("datas.csv");


tab_valid, tab_invalid = terminator.separate_students_with_tab(all_students);

print("***********TABLEAU INVALIDE**********\n",len(tab_invalid))
print("***********TABLEAU VALIDE**********\n",len(tab_valid))

