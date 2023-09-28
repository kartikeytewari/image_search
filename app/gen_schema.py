import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080"
)

# delete old schema and associated data
client.schema.delete_class("meme_image")

# create schema
class_meme = {
    'class': 'meme_image',
    'vectorizer': 'img2vec-neural', # pytorch neural network will generate vector for stored data
    'vectorIndexType': 'hnsw', # (Hierarchical navigable small worlds) specify the search algorithm
    'properties': [
        {
            'name': 'meme_image',
            'dataType': ['blob'],
        },
        {
            'name': 'meme_text',
            'dataType': ['string']
        }
    ],
    'moduleConfig': {
        'img2vec-neural': {
            'imageFields': [
                'meme_image'
            ]
        }
    }
}
client.schema.create_class(class_meme)

# print all schema in the database
db_schema = client.schema.get()
print (json.dumps(db_schema, indent=1))
