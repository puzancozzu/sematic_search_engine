indexMapping = {
    "properties":{
        "link": {
            "type":"text" 
        },
        "product_title": {
            "type":"text" 
        },
        "price": {
            "type":"text" 
        },
         "actual_price": {
            "type":"text" 
        },
         "ratings": {
            "type":"text" 
        },
         "color": {
            "type":"text" 
        },
        "DecriptionVector":{
            "type":"dense_vector",
            "dims": 768,
            "index": True,     # True - so it is searchable else it won't be searchable
            "similarity": "l2_norm",  # using euclidean distance also can be used  cosine-similarity metrics              

        }


    }
}