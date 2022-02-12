####################################################
##################LES MATRICES######################
####################################################

#Pour la creation de matrices, on utilise la fonction matrix()
#Les matrices sont presque indispensable en algébre lineaire
#Par défaut, R range les valeurs d'une matrice par colonne 
#Pour Procéder par ligne, il faut préciser l'option byrow=TRUE

m = matrix(2:26, ncol = 5, nrow = 5)

matrix(seq(10,85,by=5),nrow = 2)

matrix(1:12,nrow = 3, ncol = 4,byrow = T)

matrix(4,ncol = 10,nrow = 10)


matrix(c("A","B","C","A"),ncol=2)


n = diag(5)

m + n
m*n
t(m)

dim(m)
ncol(n)
nrow(n)


cbind(m,n)
m.length
