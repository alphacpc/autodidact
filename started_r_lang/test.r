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



################################"
row_four = "Math[14;10:12] #PC[9:12]  #Francais[14;14;12:15]  #SVT[16;11:17] #HG[16:14]  #Anglais[13;10:11]"

mondf_g = data.frame()

row_spliting <- function(row){
  row_list = strsplit(row_four, "#")
  
  for (mat in row_list[[1]]){
    label_matiere = strsplit(mat,"\\[")[[1]][1]
    notes_matiere = strsplit(strsplit(mat,"\\[")[[1]][2],"]")[[1]][1]
    devoirs = strsplit(strsplit(notes_matiere,":")[[1]][1],";")
    comp = strsplit(notes_matiere,":")[[1]][2]
   
    matrix_item = matrix(func_sep_notes(devoirs, comp),byrow=F, ncol=4)
    
    mondf = data.frame(notes=matrix_item,row.names=label_matiere)
    
    mondf_g = rbind(mondf_g,mondf)
    
  }
  return(mondf_g);
}

row_spliting(row_four)
 
