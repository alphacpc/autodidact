#FIRST INDEX == lab_es_0001
#INDEX WITHOUT MAPPING AND PROPERTIES

#CREATE 
curl -X PUT "localhost:9200/lab_es_0001?pretty"

#GET INFOS INDEX
curl -X GET "localhost:9200/lab_es_0001?pretty"

#GET MAPPING FOR INDEX
curl -X GET "localhost:9200/lab_es_0001/_mapping?pretty"

#GET SETTINGS INDEX
curl -X GET "localhost:9200/lab_es_0001/_settings?pretty"