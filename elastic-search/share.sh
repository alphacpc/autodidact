curl -X PUT 'http://127.0.0.1:9200/db_hello_test' '{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 2
  }
}'