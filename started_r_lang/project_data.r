setwd("/home/alpha/Projects/Learning/started_r_lang")
df = read.csv("datas/datas.csv")

#Create factor for label matieres
labels = c("Math","PC","SVT","Anglais","HG","Francais")
mat_fac = factor(labels)
length(mat_fac)

#Recup col notes to dataframe
col_notes = data.frame(df$Note)

# Job on rows 4 of df
#row_four = col_notes[30,]


#Define functions
func_sep_notes <- function(devs,exam){ 
  count = 1
  comp = as.numeric(exam)
  dev1 = 0
  dev2 = 0
  dev3 = 0
  
  for(i in 1:length(devs[[1]])){
    if(i == 1){
      dev1 = as.numeric(devs[[1]][i])
    }
    else if(i == 2){
      dev2 = as.numeric(devs[[1]][i])
    }
    if(i == 3){
      dev3 = as.numeric(devs[[1]][i])
    }
    else{
      next()
    }
  }
  
  return(c(dev1,dev2,dev3,comp))
}







row_spliting_dataframe <- function(row){
  mondf_g = data.frame()
  row_list = strsplit(row, "#")
  
  for (mat in row_list[[1]]){
    label_matiere = strsplit(mat,"\\[")[[1]][1]
    notes_matiere = strsplit(strsplit(mat,"\\[")[[1]][2],"]")[[1]][1]
    devoirs = strsplit(strsplit(notes_matiere,":")[[1]][1],";")
    comp = strsplit(notes_matiere,":")[[1]][2]
    
    matrix_item = matrix(func_sep_notes(devoirs, comp),byrow=F, ncol=4)
    
    mondf = data.frame(note=matrix_item,row.names=label_matiere)
    
    mondf_g = rbind(mondf_g,mondf)
    
  }
  return(mondf_g);
}

val1 = row_spliting_dataframe(col_notes[4,])
val2 = row_spliting_dataframe(col_notes[8,])

(cbind(val1,val2))
(rbind(val1,val2))
