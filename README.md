# Image Search 

- A search engine for images using weaviate

## Steps to run the project
- Run the server for vectorDB: `docker compose -f conf/docker-weaviate.yml up`
- Generate the schema: `python3 ./app/gen_schema.py`
- Load the seed images: `python3 ./app/load_data.py`
- Search for images `python3 ./app/search.py`

## Tech Stack
- Python
- Weaviate (Vector DB)
- Docker
