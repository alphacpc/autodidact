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
{"index":{}}
{"adresse": "Yeumbeul nord","age":26,"email":"alpha@gmail.com", "name": "Alpha"}
{"index":{}}
{"adresse": "Grand dakar","age":28,"email":"omar@gmail.com", "name": "Omar"}
{"index":{}}
{"adresse": "Parcelle unité 9","age":78,"email":"babs@gmail.com", "name": "Babacar"}
{"index":{}}
{"adresse": "Saly","age":33,"email":"laye@gmail.com", "name": "Ablaye"}
{"index":{}}
{"adresse": "Sédhiou","age":45,"email":"babou@gmail.com", "name": "Babacar"}
{"index":{}}
{"adresse": "Pikine nord","age":44,"email":"thierno@gmail.com", "name": "Thierno"}
{"index":{}}
{"adresse": "Tambacounda","age":50,"email":"astou@gmail.com", "name": "Astou"}
{"index":{}}
{"adresse": "Kaolack","age":33,"email":"weuz@gmail.com", "name": "Ousseynou"}
{"index":{}}
{"adresse": "Fatick","age":77,"email":"samba@gmail.com", "name": "Samba"}
{"index":{}}
{"adresse": "Fann","age":40,"email":"awa@gmail.com", "name": "Awa"}
{"index":{}}
{"adresse": "Fass","age":55,"email":"moussa@gmail.com", "name": "Moussa"}
{"index":{}}
{"adresse": "Pikine","age":44,"email":"moustapha@gmail.com", "name": "Moustapha"}
{"index":{}}
{"adresse": "Thiaroye","age":41,"email":"alioune@gmail.com", "name": "Alioune Fall"}
'
