####################################################
####################LES VECTEURS####################
####################################################


#Il existe plusieurs types de vecteurs: Numeriques, caracteres et logiques



#Les vecteurs numeriques
1:10

seq(1,12)
seq(0,100,by=10)
seq(1,4,length=10)

c(1,10,20,40,60)

rep(44,14)
rep(c(7,13),each=5)




#Les vecteurs caracteres
c("Bonjour","Salam","Hello","Diamarama")
rep(c("Bonjour","Salam","Hello","Diamarama"),each=2)
rep(c("Bonjour","Salam","Hello","Diamarama"),times=3)


#Creation par concaténation d'un vecteurs caractères
c(1:4,rep("ind",4),sep="-")
paste(1:4,rep("ind",4),sep="-")
paste(1:4,rep("ind",4),sep="-",collapse ="+")


chaine_afric = substr("Coupe d'afrique des nation", 9,15)
chaine_afric






#Les vecteurs logiques
x <- c(12,23,-2,3,-16,28,30,5,-15,38)
test <- x>20
test
