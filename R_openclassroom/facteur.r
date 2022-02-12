####################################################
################LES FACTEURS########################
####################################################


#Les factory nous permettent de catégoriser notre population 
#Tres utile quand, on travaille sur un jeu de données

elements = c("Homme","Femme","Femme","Femme","Homme", "Homme","Femme","Homme","Homme")
category = factor(elements)

category

nlevels(category)

levels(category)
levels(category) <- c("F","H")
levels(category)

X <- c(rep(10,3),rep(12,2),rep(13,4))
X
is.factor(X)
is.numeric(X)
summary(X)


xFactory <- factor(X)
xFactory
mode(xFactory)
