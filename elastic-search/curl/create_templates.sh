curl -X PUT "localhost:9200/_template/lab_es_0002" -H 'Content-Type: application/json' -d'
{
  "index_patterns": ["lab_es_*"],
  "settings": 
  {
    "number_of_shards" : 1,
    "number_of_replicas" : 0   
  }
}
'