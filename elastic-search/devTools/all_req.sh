GET lab_es_0002

GET lab_es_0002/_search

GET lab_es_0002/_mapping/

GET lab_es_0002/_settings

GET lab_es_0002/_alias

DELETE lab_es_0002

GET /lab_es_0002/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age":   26 }}
      ]
    }
  }
}



GET /lab_es_0002/_search
{
  "query": { 
    "bool": { 
      "must": [
        { "match": { "name":   "alpha"  }}
      ],
      "filter": [ 
        { "range": { "age": { "gte": 20 }}}
      ]
    }
  }
}


GET /lab_es_0002/_search
{
  "query": { 
    "bool": {
      "filter": {
          "term": {
            "name" :"tely"
          }
        }
    }
  }
}


GET /lab_es_0002/_search
{
  "query": { 
    "bool": { 
      "filter": [ 
        { "range": { "age": { "gte": 25, "lte": 30 }}}
      ]
    }
  }
}


GET lab_es_residents

GET lab_es_residents/_search

GET lab_es_residents/_search
{
  "query": 
  {
    "match": {
      "adresse": "foire"
    }
  }
}




GET lab_es_residents/_search
{
  "query": 
  {
    "match": {
      "fullname": "diallo"
    }
  }
}


#Recherche avec score en description

GET lab_es_residents/_search?explain=true
{
  "query": 
  {
    "match": {
      "fullname": "diallo"
    }
  }
}

#Recherche avec OR

GET lab_es_residents/_search
{
  "query": 
  {
    "match": {
      "fullname": "diallo amadou"
    }
  }
}

GET lab_es_residents/_search
{
  "query": 
  {
    "match": {
      "adresse": "auchan nord"
    }
  }
}


#Recherche AND
GET lab_es_residents/_search
{
  "query": 
  {
    "match": 
    {
      "adresse":
      {
        "query": "foire auchan",
        "operator": "and"
      }
    }
  }
} 



#Recherche avec multichamps
GET lab_es_residents/_search
{
  "query": 
  {
    "bool": 
    {
      "should": 
      [
        {"match": {"fullname": "diallo"}},
        {"match": {"adresse": "ouest"}}
      ]  
    }
  }
}




###########################################
######Recherche de type Dismax#############
GET lab_es_residents/_search
{
 "query":
 {
   "dis_max": {
     "queries":
     [
       {"match": {"adresse": "diallo"}},
       {"match": {"fullname": "diallo"}}
     ]
   }
 }
}




#Recherches de type Dismax avec tiebreaker
GET lab_es_residents/_search
{
 "query":
 {
   "dis_max": {
     "queries":
     [
       {"match": {"adresse": "diallo"}},
       {"match": {"fullname": "diallo"}}
     ],
     "tie_breaker": 0.8
   }
 }
}


#Queries de type Multimatch
GET lab_es_residents/_search
{
  "query": 
  {
    "multi_match": {
      "type": "best_fields", 
      "query": "diallo",
      "fields": ["adresse","fullname"],
      "tie_breaker": 0.3
      
    }
  }
}




#Multimatch avec pondération de champs
GET lab_es_residents/_search
{
  "query": 
  {
    "multi_match": {
      "type": "best_fields", 
      "query": "diallo",
      "fields": ["adresse^3","fullname^0.2"],
      "tie_breaker": 0.3
    }
  }
}







GET lab_es_happy

GET lab_es_happy/_search


#Analyse des données indexées par token pour chaque mot
GET /lab_es_happy/_analyze
{
  "field": "app_name",
  "text" : "Je suis tres content. j'aime le mafé"
}


#match ou match_phrase
GET lab_es_happy/_search
{
  "query": 
  {
    "match": {
      "title": "livraison client"
    }
  }
}


#Regarde seulement la phrase conserner ainsi que la succession des mots
GET lab_es_happy/_search
{
  "query": 
  {
    "match_phrase": 
    {
      "title" : "suis content"
    }
  }
}




GET lab_es_happy/_search
{
  "query": 
  {
    "match": 
    {
      "title":
      {
        "query": "je pas content",
        "operator": "and"
      }
    }
  }
} 





###Recherche Partial matching
GET lab_es_0002/_mapping

GET lab_es_0002/_search


#Recherche de tous les emails qui débutent par "al"
GET lab_es_0002/_search
{
  "query" :
  {
    "prefix": {
      "email": {
        "value": "al"
      }
    }
  }
}


#Recherche de tous les mots contenant les caractéres "ph" sur le champs name
GET lab_es_0002/_search
{
  "query" :
  {
    "regexp": {
      "name": {
        "value": ".*ph.*"
      }
    }
  }
}



#Recherche des documents dont l'adresse commence par "Fa"
GET lab_es_0002/_search
{
  "query" :
  {
    "match_phrase_prefix": {
      "adresse": "Fa"
    }
  }
}





######Recherche avec spécifivité du langage
PUT lab_lang
{
  "mappings": {
  "properties" : 
  {
    "app_name" : 
    {
      "type" : "text",
      "fields" :
      {
        "english" :
        {
          "type" : "text",
          "analyzer" : "english"
        }
      }
    },
    "type" : 
    {
      "type" : "keyword"
    },          
    "genres" : 
    {
      "type" : "text",
      "fields" :
      {
        "english" :
        {
          "type" : "text",
          "analyzer" : "english"
        }
      }
    },
    "category" :
    {
      "type" : "keyword"
    },
    "price" :
    {
      "type" : "double"
    },
    "last_updated" :
    {
      "type" : "date"
    },
    "content_rating" :
    {
      "type" : "text",
      "fields" :
      {
        "keyword" : 
        {
          "type" : "keyword"
        }
      }
    },
    "rating" :
    {
      "type" : "double"
    }     
  }
    
  }
}


POST /lab_lang/_bulk
{ "index": { "_id": 1 }}
{"app_name" : "Photo Editor & Candy Camera & Grid & ScrapBook", "type" : "Free", "genres" : "Art & Design", "category" : "ART_AND_DESIGN","price" : 0.0, "last_updated" : "2018-01-06T23:00:00.000Z", "content_rating" : "Everyone","rating" : 4.1}
{ "index": { "_id": 2 }}
{ "app_name" : "Pixel Draw - Number Art Coloring Book", "type" : "Free", "genres" : "Art & Design;Creativity", "category" : "ART_AND_DESIGN",           "price" : 0.0, "last_updated" : "2018-06-19T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.3}
{ "index": { "_id": 3 }}
{ "app_name" : "Garden Coloring Book", "type" : "Free", "genres" : "Art & Design", "category" : "ART_AND_DESIGN", "price" : 0.0, "last_updated" : "2017-09-19T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.4}
{ "index": { "_id": 4 }}
{ "app_name" : "Tattoo Name On My Photo Editor", "type" : "Free", "genres" : "Art & Design", "category" : "ART_AND_DESIGN",           "price" : 0.0, "last_updated" : "2018-04-01T22:00:00.000Z", "content_rating" : "Teen", "rating" : 4.2}
{ "index": { "_id": 5 }}      
{ "app_name" : "YouTube Kids", "type" : "Free", "genres" : "Entertainment;Music & Video", "category" : "FAMILY",           "price" : 0.0, "last_updated" : "2018-08-02T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.5}
{ "index": { "_id": 6 }}      
{ "app_name" : "Candy Bomb", "type" : "Free", "genres" : "Casual;Brain Games", "category" : "FAMILY",           "price" : 0.0, "last_updated" : "2018-07-03T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.4}
{ "index": { "_id": 7 }}      
{ "app_name" : "ROBLOX", "type" : "Free", "genres" : "Adventure;Action & Adventure", "category" : "FAMILY",           "price" : 0.0, "last_updated" : "2018-07-30T22:00:00.000Z", "content_rating" : "Everyone 10+", "rating" : 4.5}
{ "index": { "_id": 8 }}      
{ "type" : "Free", "genres" : "Casual;Brain Games", "category" : "FAMILY",           "price" : 0.0, "last_updated" : "2018-07-22T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.4}
{ "index": { "_id": 9 }}      
{ "app_name" : "Bowmasters", "type" : "Free", "genres" : "Action", "category" : "GAME",           "price" : 0.0, "last_updated" : "2018-07-22T22:00:00.000Z", "content_rating" : "Teen", "rating" : 4.7}
{ "index": { "_id": 10 }}      
{ "app_name" : "Magic Tiles 3", "@timestamp" : "2019-03-02T07:03:20.040Z", "type" : "Free", "genres" : "Music", "category" : "GAME", "price" : 0.0, "last_updated" : "2018-08-02T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.5}
{ "index": { "_id": 11 }}      
{ "app_name" : "Block Puzzle Classic Legend !", "@timestamp" : "2019-03-02T07:03:20.040Z", "type" : "Free", "genres" : "Puzzle", "category" : "GAME",           "price" : 0.0, "last_updated" : "2018-04-12T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.2}
{ "index": { "_id": 12 }}      
{ "app_name" : "Marble Woka Woka 2018 - Bubble Shooter Match 3", "type" : "Free", "genres" : "Puzzle", "category" : "GAME",           "price" : 0.0, "last_updated" : "2018-08-02T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.6}
{ "index": { "_id": 13 }}      
{ "app_name" : "QR Code Reader", "type" : "Free", "genres" : "Tools", "category" : "TOOLS",           "price" : 0.0, "last_updated" : "2016-03-15T23:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.0}
{ "index": { "_id": 14 }}      
{ "app_name" : "SHAREit - Transfer & Share", "type" : "Free", "genres" : "Tools", "category" : "TOOLS",           "price" : 0.0, "last_updated" : "2018-07-29T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.6}
{ "index": { "_id": 15 }}      
{ "app_name" : "Diabetes:M", "type" : "Free", "genres" : "Medical", "category" : "MEDICAL", "price" : 0.0, "last_updated" : "2018-07-31T22:00:00.000Z", "content_rating" : "Everyone", "rating" : 4.6}

#Approche naive
GET lab_lang/_search
{
  "query": 
  {
    "multi_match": {
      "query": "photos",
      "fields": ["app_name"]
    }
  }
}



GET lab_lang/_search
{
  "query": 
  {
    "multi_match": {
      "query": "photos",
      "fields": ["app_name"]
    }
  }
}


GET lab_lang/_search
{
  "query": 
  {
    "multi_match": {
      "query": "photos",
      "fields": ["app_name","app_name.english"]
    }
  }
}

GET lab_lang/_search
{
  "query": 
  {
    "multi_match": {
      "query": "photos",
      "fields": ["app_name^4","app_name.english"]
    }
  }
}