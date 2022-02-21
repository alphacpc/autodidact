# INSTALL ELASTIC SEARCH WITH DOCKER

## docker pull docker.elastic.co/elasticsearch/elasticsearch:7.6.2

## docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.6.2

## docker images

## docker ps -a

### Utilisation de **curl**
- GET : *récupérer  de la data*
- PUT : *création de data*
- POST : *mis à jour*
- bulk : *enchainer les insertions*

### Creation de base de données (appelé *index* sur Elastic Search)
Type (table) : utilisateurs <br>
proprétés (champs) : nom/prenom/age/adresse <br>
