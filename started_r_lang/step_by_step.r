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
row_four_list = strsplit(row_four, "#")

#Get single matiere
get_math = row_four_list[[1]][1]

#Split get_mat
list_math = strsplit(get_math, "\\[")
label_mat = list_math[[1]][1]
notes_mat = list_math[[1]][2]
get_note_mat = strsplit(notes_mat,"]")[[1]][1]


#Split notes mat
devoirs = strsplit(strsplit(get_note_mat,":")[[1]][1],";")
comp = strsplit(get_note_mat,":")[[1]][2]
devoirs[[1]][2]


row_spliting("Math[04;13:05] #Francais[15;16:14] #Anglais[15;16:11] #PC[04;03:07] #SVT[12;09:11] #HG[16;15:10]")
#Loop row for getting infos
for (element in row_four_list){
  print(element)
}


