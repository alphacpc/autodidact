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