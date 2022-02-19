setwd("/home/alpha/Projects/Learning/started_r_lang")
df = read.csv("datas/datas.csv")

#Create factor for label matieres
labels = c("Math","PC","SVT","Anglais","HG","Francais")
mat_fac = factor(labels)
length(mat_fac)

#Recup col notes to dataframe
col_notes = data.frame(df$Note)

# Job on rows 4 of df
row_four = col_notes[4,]


#Define function to split all rows
row_spliting <- function(row){
  row_list = strsplit(row_four, "#")
  print(row_list)
  for (mat in row_list[[1]]){
    
    label_matiere = strsplit(mat,"\\[")[[1]][1]
    notes_matiere = strsplit(strsplit(mat,"\\[")[[1]][2],"]")[[1]][1]
    devoirs = strsplit(strsplit(notes_matiere,":")[[1]][1],";")
    comp = strsplit(notes_matiere,":")[[1]][2]
    #print(label_matiere)
    #print(devoirs)
    #print(comp)
  }
  return(c(label_matiere,devoirs,comp))
}

row_spliting(row_four)


