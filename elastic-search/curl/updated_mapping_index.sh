#ADDED MAPPING FIELD ON EXISTANT INDEX WITH MAPPING
curl -X PUT "localhost:9200/lab_es_0002/_mapping?pretty" -H 'Content-Type: application/json' -d'
{
  "properties": {
    "adresse": {
      "type": "text"
    }
  }
}
'


#SELECT THE MAPPING OF SPECIFIC FIELDS
curl -X GET "localhost:9200/lab_es_0002/_mapping/field/age?pretty"
