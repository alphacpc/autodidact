students <- read.table("./Projects/Learning/R_openclassroom//eleves.csv", sep=",", header=TRUE, dec=",")
notes <- read.table("./Projects/Learning/R_openclassroom//notes.csv", sep=";", header=TRUE, dec=",")

summary(students)
summary(notes)


is.na(students)
is.na(notes)

notes
col_notes <- notes[,4]

mondf <- merge(students,notes)
mondf
summary(mondf)
which(is.na(mondf), arr.ind = T)
hist(col_notes)


names(mondf)[3]

mondf[names(mondf)[3] > 20]
mondf[names(mondf)[7]]

mondf[28:54,]
summary(mondf[28:54,])
summary(mondf[1:28,])


which(mondf==20, arr.ind = T)
mondf[49,]
mondf[53,]
mondf[54,]


#Pour voir l'élève qui as 20
View(mondf[mondf$notes==20,])


#Pour voir la moyenne des filles
mean(mondf[mondf$sexe == 'F', 'notes'], na.rm=TRUE)

#Pour voir la moyenne des garçons
mean(mondf[mondf$sexe == 'M', 'notes'], na.rm=TRUE)





#Pour voir la moyenne des devoir de Maths et SVT
mean(mondf[mondf$matiere == 'Math', 'notes'], na.rm=T)
mean(mondf[mondf$matiere == 'SVT', 'notes'], na.rm=T)
