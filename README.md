# Image Search 

- A search engine for images using weaviate

## Steps to run the project
- Run the server for vectorDB: `docker compose -f conf/docker-weaviate.yml up`
- Go to app folder: `cd app`
- Install virtual environment: `python3 -m venv venv && source ./venv/bin/activate && pip3 install -r requirements.txt`
- Generate database schema: `python3 gen_schema.py`
- Load seed images: `python3 load_data.py`
- Search for images: `python3 search.py`

## Tech Stack
- Python
- Docker
- Weaviate (Vector DB)
