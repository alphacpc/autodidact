#ADDED USER
curl -X POST "localhost:9200/lab_es_0002/_bulk?refresh=true&pretty" -H 'Content-Type: application/json' -d'
{"index":{}}
{"adresse": "Keur massar","age":29,"email":"abasse@gmail.com", "name": "Abasse"}
{"index":{}}
{"adresse": "Rufisque","age":22,"email":"mariama@gmail.com", "name": "Mariama"}
{"index":{}}
{"adresse": "Cite Asecna","age":22,"email":"ibrahima@gmail.com", "name": "Ibrahima"}
{"index":{}}
{"adresse": "Cite Asecena Ouakam","age":44,"email":"mouhamed@gmail.com", "name": "Mouhamed"}
{"index":{}}
{"adresse": "Yeumbeul","age":54,"email":"saliou@gmail.com", "name": "Saliou"}
{"index":{}}
{"adresse": "Fass","age":25,"email":"fatou@gmail.com", "name": "Fatou"}
{"index":{}}
{"adresse": "Pikine","age":30,"email":"cheikh@gmail.com", "name": "Cheikh dieng"}
{"index":{}}
{"adresse": "Grand yoff","age":26,"email":"tely@gmail.com", "name": "Amadou tely"}
{"index":{}}
{"adresse": "Rufisque","age":26,"email":"mariem@gmail.com", "name": "Marieme"}
'
