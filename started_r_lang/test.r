helloWord <- function(devs,exam){ 
  count = 1
  for(i in devs){
    if(count == 1){
      dev1 = i
    }
    
    count <- count + 1
  }
  comp = exam
  
  return (c(dev1,dev2,dev3, comp))
}

helloWord(list("12","14"), "20")

list("12" "14")[[1]]
