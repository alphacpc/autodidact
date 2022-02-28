curl -PUT 'http://localhost:9200/lab_es_1_curl_test/docs?pretty' -H 'Content-Type: application/json' -d '
{
  "mappings": {
    "properties": {
      "age":    { "type": "integer" },  
      "email":  { "type": "keyword"  }, 
      "name":   { "type": "text"  }     
    }
  }
}
'