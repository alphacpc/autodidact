/* SELECT ALL MARQUE == Lamborghini */
SELECT * FROM vehicule WHERE marque='Lamborghini';

/* SELECT ALL MARQUE == Lamborghini sans la colonne marque  */
SELECT id_veh, annee, modele FROM vehicule WHERE marque='Lamborghini';

/* SELECT Column marque */
SELECT marque  FROM vehicule;

/*Select toutes les informations d'une piece*/
SELECT * FROM piece, reference WHERE piece.id_ref=reference.id_ref;

/*Select toutes les informations d'une piece*/
SELECT * FROM piece, reference WHERE piece.id_ref=reference.id_ref;

/*Select toutes les informations d'une piece sans répétition des colonnes id_ref*/
SELECT id_p, categorie, date_recup, piece.id_ref, prix FROM piece, reference WHERE piece.id_ref=reference.id_ref ORDER BY prix;

/*Select toutes les informations d'une piece sans répétition des colonnes id_ref avec ordre croissant des prix*/
SELECT id_p, categorie, date_recup, piece.id_ref, prix FROM piece, reference WHERE piece.id_ref=reference.id_ref AND prix >1500000 ORDER BY prix;

/*Pour calculer la moyenne avec la fonction AVG*/
SELECT AVG(prix) FROM reference;

/*Select toutes les pieces dont le prix est supérieur à la moyenne*/
SELECT id_p, categorie, date_recup, piece.id_ref, prix FROM piece, reference WHERE piece.id_ref=reference.id_ref AND prix > (SELECT AVG(prix) FROM reference) ORDER BY prix;


/*SELECT TOUTES LES MARQUES DE MANIERE UNIQUE*/
SELECT DISTINCT marque FROM vehicule;

/*COMPTER LE NOMBRE DE CATEGORIE DANS LA TABLE PIECE*/
SELECT count(categorie) FROM piece;

/*AFFICHER LA CATEGORIE ET LE NOMBRE D'OCCURENCE DANS LA TABLE PIECE*/
SELECT categorie,count(categorie) FROM piece GROUP BY categorie;

/*SELECT LA CATEGORIE, LE NOMBRE D'OCCURENCE ET LA SOMME CUMULÉE POUR UNE CATEGORIE*/
SELECT categorie, count(categorie), sum(prix) FROM piece, reference WHERE piece.id_ref= reference.id_ref GROUP BY categorie;



/* HAVING == SELECT D'UNE SELECT*/
/*FAIRE UN TEST SUR UNE FONCTION ON UTILISE HAVING*/
SELECT categories, count(categories), sum(prix) as somme FROM pieces, reference WHERE pieces.id_ref= reference.id_ref GROUP BY categories HAVING somme > 500000;

SELECT * FROM (SELECT categories, count(categories), sum(prix) as somme FROM pieces, reference WHERE pieces.id_ref= reference.id_ref GROUP BY categories)as tab WHERE tab.somme > 430000;


/*PRENDRE TOUTES LES CATEGORIE QUI DÉBUTE PAR 'G'*/
SELECT * FROM pieces WHERE categories LIKE 'g%';


/*AFFICHER TOUTES LES MARQUES QUI NE CONTINENT PAS LA LETTRE 'g', IL SUFFIT D'UTILISER LES %...%*/
SELECT * FROM vehicule WHERE marque NOT LIKE '%g%';


/*AFFICHER LES PIECES FABRIQUÉS DU 1er Jan 2015 au 31 Dec 2017*/
SELECT * FROM pieces WHERE dates BETWEEN '2015-01-01' AND '2017-12-31';

SELECT * FROM pieces WHERE year(dates) BETWEEN 2015 AND 2017;

/*AFFICHE LES PIECES DE 3 À 10*/
SELECT * FROM pieces LIMIT 10 offset 2;
SELECT * FROM pieces limit 2 , 10;



/*Faire la somme pour une categorie donné*/
select general.id_veh, general.marque, sum(general.prix) from (select big.id_p, big.id_veh, big.marque, big.annee, big.modele, big.id_ref,reference.prix from(select grand.id_p, grand.id_veh, grand.marque, grand.annee, grand.modele, piece.categorie, piece.date_recup, piece.id_ref from (select tab.id_p,vehicule.id_veh, vehicule.marque, vehicule.annee, vehicule.modele  from (select * from correspondance where id_veh = 2) as tab , vehicule where tab.id_veh = vehicule.id_veh) as grand , piece where grand.id_p = piece.id_p) as big, reference where big.id_ref= reference.id_ref) as general GROUP BY general.id_veh, general.marque,general.prix ;
