curl -X  PUT 'localhost:9200/mydatabase' -d '
    {"mappings" : {
        "utilisateurs" : {
            "properties" : {
                "nom" : { "type" :  "string"},
                "prenom" : { "type" :  "string"},
                "age" : { "type" :  "int"},
                "adresse" : { "type" :  "string"}
}}}}'