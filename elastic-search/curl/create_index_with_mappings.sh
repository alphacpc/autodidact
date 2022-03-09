#CREATE INDEX WITH MAPPING AND PROPERTIES FIELDS
curl -X PUT "localhost:9200/lab_es_0002?pretty" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
      "name":    { "type": "text" },  
      "email":  { "type": "keyword"  }, 
      "age":   { "type": "integer"  }     
    }
  }
}
'
