#ADDED USER
curl -X POST "localhost:9200/lab_es_residents/_bulk?refresh=true&pretty" -H 'Content-Type: application/json' -d'
{"index":{}}
{"fullname": "Alpha amadou diallo", "adresse": "Yeumbeul nord"}
{"index":{}}
{"fullname": "Thierno soulayemane Baal", "adresse": "Région de matam"}
{"index":{}}
{"fullname": "Alain latouff", "adresse": "Ouest foire à coté auchan"}
{"index":{}}
{"fullname": "Abdou Deme", "adresse": "Ouest foire"}
{"index":{}}
{"fullname": "Ndeye fatou diop", "adresse": "Nord foire"}
{"index":{}}
{"fullname": "Adja sene", "adresse": "Nord foire "}
{"index":{}}
{"fullname": "Abdou diallo", "adresse": "Paris boulevard 16"}
{"index":{}}
{"fullname": "awa diallo", "adresse": "Thiaroye taly diallo"}
'
