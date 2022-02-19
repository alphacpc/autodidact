####################################################
####################LES LISTES######################
####################################################



#Les listes somme comme les matrices sauf que les listes ne sont pas nomotypes
maliste <- list(c("A","B","C","A"),matrix(1:6,2,3), rep(1,10))
maliste


length(maliste)

mode(maliste)

names(maliste)

names(maliste) <- c("vec","mat","uni")

names(maliste)

maliste
