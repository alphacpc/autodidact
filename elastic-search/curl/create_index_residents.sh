#CREATE INDEX WITH MAPPING AND PROPERTIES FIELDS
curl -X PUT "localhost:9200/lab_es_residents?pretty" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
      "fullname":    { "type": "text" },  
      "adresse":  { "type": "text"  }    
    }
  }
}
'