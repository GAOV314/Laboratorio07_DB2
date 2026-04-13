import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
# Usamos el USERNAME y PASSWORD del .env
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

# El driver solo necesita URI y AUTH. 
# El '+ssc' en tu URI ya maneja el problema del certificado.
driver = GraphDatabase.driver(URI, auth=AUTH)