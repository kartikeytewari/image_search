import weaviate
import pybase64

client = weaviate.Client(
    url="http://localhost:8080"
)

# read the test image
test_image = "2.png"
with open("../data/test/" + test_image, "rb") as local_image:
    image_embedding = pybase64.b64encode(local_image.read())
    image_embedding = image_embedding.decode('utf-8')

    result_embedding = (
        client.query
        .get("meme_image", ["meme_image", "meme_text"])
        .with_near_image({
            "image": image_embedding,
            "distance": 0.4
        },
        encode=False)
        .with_limit(1)
        .do()
    )

    print (result_embedding)

    result_image = result_embedding["data"]["Get"]["Meme_image"][0]["meme_image"]
    result_text = result_embedding["data"]["Get"]["Meme_image"][0]["meme_text"]
    
    result_image = pybase64.b64decode((result_image))
    img_file = open('out.png', 'wb')
    img_file.write(result_image)
    img_file.close()

    print (result_text)
