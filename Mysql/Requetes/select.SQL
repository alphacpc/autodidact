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
SELECT id_p, categorie, date_recup, piece.id_ref, prix FROM piece, reference WHERE piece.id_ref=reference.id_ref AND prix >1500000 order by prix;

/*Pour calculer la moyenne avec la fonction AVG*/
SELECT AVG(prix) FROM reference;

/*Select toutes les pieces dont le prix est supérieur à la moyenne*/
SELECT id_p, categorie, date_recup, piece.id_ref, prix FROM piece, reference WHERE piece.id_ref=reference.id_ref AND prix > (SELECT AVG(prix) FROM reference) order by prix;


/*Select toutes les marques une seule fois*/
SELECT DISTINCT marque FROM vehicule;

/*Compte le nombre de categorie dans la table piece*/
SELECT count(categorie) FROM piece;

/*Prendre la categorie et le nombre de fois qu'il est present dans la table piece*/
SELECT categorie,count(categorie) FROM piece GROUP BY categorie;

