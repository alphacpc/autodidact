curl -X POST "localhost:9200/lab_es_happy/_bulk?refresh=true&pretty" -H 'Content-Type: application/json' -d'
{ "index": { "_id": 1 }}
{ "title": "Je ne suis pas content. Service client nul" }
{ "index": { "_id": 2 }}
{ "title": "Je suis content. Pas de retard de livraison" }
{ "index": { "_id": 3 }}
{ "title": "Je suis tres content. pas de probleme" }
'