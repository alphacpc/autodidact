setwd("/home/alpha/Projects/Learning/R_openclassroom/")
df = read.csv("datas.csv")

labels = c("Math","PC","SVT","Anglais","HG","Français")
fac = factor(labels)

notes = data.frame(df$Note)
notes

single = notes[1,]
single

sep = strsplit(single, split = "#")
sep

length(sep[[1]])

for (el in sep){
  print(el)
}


