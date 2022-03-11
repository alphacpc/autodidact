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