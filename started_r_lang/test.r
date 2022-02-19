func_sep_notes <- function(devs,exam){ 
  count = 1
  comp = as.numeric(exam)
  dev1 = 0
  dev2 = 0
  dev3 = 0
  
  for(i in 1:length(devs)){
    if(i == 1){
      dev1 = as.numeric(devs[i])
    }
    else if(i == 2){
      dev2 = as.numeric(devs[i])
    }
    if(i == 3){
      dev3 = as.numeric(devs[i])
    }
    else{
      next()
    }
  }
  
  return(c(dev1,dev2,dev3,comp))
}

func_sep_notes(c("18"), "20")
