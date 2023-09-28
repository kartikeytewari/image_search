import weaviate
import pybase64

client = weaviate.Client(
    url="http://localhost:8080"
)

for i in range(1,11):
    print ("image_processing-" + str(i))
    
    # generate image blob
    with open ("../data/seed_image/image_data/" + str(i) + ".png", "rb") as local_image:
        image_embedding = pybase64.b64encode(local_image.read())
        image_embedding = image_embedding.decode('utf-8')

    # generate image text 
    with open ("../data/seed_image/text_data/" + str(i) + ".txt", "rb") as local_text:
        text_embedding = local_text.read()
        text_embedding = text_embedding.decode('utf-8')

    # add object
    local_uuid = client.data_object.create({
        'meme_image': image_embedding,
        'meme_text': text_embedding
    }, 'meme_image')

    print ("local_uuid = ", local_uuid)