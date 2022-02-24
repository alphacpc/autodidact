curl -X PUT 'http://127.0.0.1:9200/db_hello' -H 'Content-Type: application/json' -d "{
  'mappings': {      
    'properties': {
        'fname': {'type': 'text'},
        'lname': {'type': 'text'},
        'age': {'type': 'integer'},
        'adress': {'type': 'text'},
        }
    }
}"