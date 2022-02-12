####################################################
################Premier pas avec R##################
####################################################



#La creation d'object par l'affectation
x <- 2 #Pour créer l'objet x en lui donnant la valeur 2
y = 4 #y recoit la valeur 4
14 -> z #z recoit la valeur 14 



#Pour l'affichage d'un objet en R, on peut utiliser la fonction print() ou passer par le nom de l'object directement
print(x)
x


#En revanche, on peut supprimer un objet avec la méthode rm()
rm(z)
z



#Les types d'objets: NULL, LOGICAL, NUMERIC, COMPLEX, CHARACTER
fullname = "Jules Laporte"
age = 25
addresse = "Suisse, Luisance"
poids = 74
taille = 1.80
nb_enfants = NULL
maried = FALSE




#Pour connaitre le mode d'objet il exite la méthode mode() en d'autres therme le type
mode(fullname)
mode(age)
mode(taille)
mode(maried)
mode(nb_enfants)
mode(poids)




#Tester l'appartenance d'un objet par "is"
is.numeric(fullname)
is.numeric(age)
is.logical(maried)
is.logical(poids)



#La conversion par "as"
as.character(age)
mode(age)
as.character(maried)
mode(maried)

