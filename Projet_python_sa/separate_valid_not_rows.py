tab_valid = [];
tab_invalid = [];


def separate_rows(tabs):

    for row in tabs:
        if len(row["Numero"]) != 7:
            tab_invalid.append(row);
        else:
            tab_valid.append(row);
    
    return tab_valid, tab_invalid;

