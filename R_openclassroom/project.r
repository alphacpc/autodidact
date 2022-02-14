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



