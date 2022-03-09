#ADDED USER
curl -X POST "localhost:9200/lab_es_0002/_bulk?refresh=true&pretty" -H 'Content-Type: application/json' -d'
{"index":{}}
{"adresse": "Yeumbeul Nord","age":25,"email":"alphacpc@gmail.com", "name": "alpha"}
{"index":{}}
{"adresse": "Cite Asecna","age":24,"email":"makhou@gmail.com", "name": "Matar"}
'
