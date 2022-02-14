students <- read.table("./Projects/Learning/R_openclassroom//eleves.csv", sep=",", header=TRUE, dec=",")
notes <- read.table("./Projects/Learning/R_openclassroom//notes.csv", sep=";", header=TRUE, dec=",")

mondf = merge(students,notes,by='identifiant')
mondf


#Je veux recuperer les devoirs de maths
mondf$matieres
mondf$matieres=="Math"
mondf[mondf$matiere == 'Math', 'notes']

#Je récuperer les devoirs de SVT
mondf[mondf$matiere == 'SVT', 'notes']


#Je récupere la note des filles
mondf[mondf$sexe == 'F', 'notes']

