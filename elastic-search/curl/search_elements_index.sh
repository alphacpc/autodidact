######################################################
######################################################
##############RECHERCHE PAR MATCH#####################
######################################################
######################################################

#SEARCH ALL FIELD
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}
'

#SEARCH BY FIELD NAME
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
        "name": "Alpha"
    }
  }
}
'

#SEARCH BY FIELD AGE
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
        "age": 15
    }
  }
}
'

#SEARCH BY EMAIL
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
        "email": "alphacpc@gmail.com"
    }
  }
}
'

#SEARCH WITH MUST FOR AGE
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age":   25  }}
      ]
    }
  }
}
'



######################################################
######################################################
##############RECHERCHE PAR FILTER####################
######################################################
######################################################

#SEARCH WITH RANGE AGE
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { 
    "bool": { 
      "filter": [ 
        { "range": { "age": { "gte": 20 }}}
      ]
    }
  }
}
'

curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { 
    "bool": { 
      "filter": [ 
        { "range": { "age": { "gte": 20, "lte":30 }}}
      ]
    }
  }
}
'

#SEARCH WITH RANGE AGE AND NAME CONTAINT ALPHA
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { 
    "bool": { 
      "must": [
        { "match": { "name":   "alpha"  }}
      ],
      "filter": [ 
        { "range": { "age": { "gte": 20 }}}
      ]
    }
  }
}
'

#SEARCH WITH TERMs
curl -X GET "localhost:9200/lab_es_0002/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { 
    "bool": {
      "filter": 
        {
          "term": {
            "name" :"matar"
          }
        }
    }
  }
}
'









######################################################
######################################################
##############REQUETE DE TYPE FULL TEXT###############
######################################################
######################################################

################Recherche sur un champs unique########
####Rechercher le mot-clé FOIRE
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "match": {
      "adresse": "foire"
    }
  }
}'


###Recherche "diallo"
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "match": {
      "fullname": "diallo"
    }
  }
}'

###Recherche "diallo" avec description du score
curl -X GET "localhost:9200/lab_es_residents/_search?explain=true" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "match": {
      "fullname": "diallo"
    }
  }
}'


###Recherche avec plusieurs mots clés --OR--
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "match": {
      "adresse": "foire ouest"
    }
  }
}'




###Recherche avec plusieurs mots clés --AND--
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "match": 
    {
      "adresse":
      {
        "query": "foire auchan",
        "operator": "and"
      }
    }
  }
}'





################Recherche multiples champs###########
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "bool": 
    {
      "should": 
      [
        {"match": {"fullname": "diallo"}},
        {"match": {"adresse": "ouest"}}
      ]  
    }
  }
}'










######################################################
######################################################
##############REQUETE DE TYPE FULL TEXT###############
######################################################
######################################################

################Recherche de type dismax##############
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
 "query":
 {
   "dis_max": {
     "queries":
     [
       {"match": {"adresse": "nord"}},
       {"match": {"fullname": "diallo"}}
     ]
   }
 }
}'


#Queries de type Multimatch
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "multi_match": {
      "type": "best_fields", 
      "query": "diallo",
      "fields": ["adresse","fullname"],
      "tie_breaker": 0.3
      
    }
  }
}'


#Multimatch avec pondération de champs
curl -X GET "localhost:9200/lab_es_residents/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": 
  {
    "multi_match": {
      "type": "best_fields", 
      "query": "diallo",
      "fields": ["adresse^3","fullname^0.2"],
      "tie_breaker": 0.3
    }
  }
}'










#LA PARTIE PROXIMITÉ
curl -X GET "localhost:9200/lab_es_happy/_analyze?pretty" -H 'Content-Type: application/json' -d'
{
  "field": "app_name",
  "text" : "Je suis tres content. avoir des 5 enfants"
}'