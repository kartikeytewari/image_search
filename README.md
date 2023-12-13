# Image Search 

- A search engine for images using weaviate

## Steps to run the project
- Run the server for vectorDB: `docker compose -f conf/docker-weaviate.yml up`
- Go to app folder: `cd app`
- Source python virtual environment: `source ./venv/bin/activate`
- Generate the database schema: `python3 gen_schema.py`
- Load the seed images: `python3 load_data.py`
- Search for images: `python3 search.py`

## Tech Stack
- Python
- Weaviate (Vector DB)
- Docker
