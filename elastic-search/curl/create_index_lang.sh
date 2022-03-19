curl -X POST "localhost:9200/lab_lang/_bulk?refresh=true&pretty" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties" : 
        {
            "app_name" : {
                "type" : "text",  "fields" :{
                    "english" : { 
                        "type" : "text", "analyzer" : "english" 
                    }
                }
            },
            "type" : {
                "type" : "keyword"
            },          
            "genres" : {
                "type" : "text", "fields" : {
                    "english" : {
                        "type" : "text",
                        "analyzer" : "english"
                    }
                }
            },
            "category" : {
                "type" : "keyword"
            },
            "price" : {
                "type" : "double"
            },
            "last_updated" : {
                "type" : "date"
            },
            "content_rating" : {
                "type" : "text", "fields" : {
                    "keyword" :  {
                        "type" : "keyword"
                    }
                }
            },
            "rating" : {
                "type" : "double"
            }     
        }
    }
}