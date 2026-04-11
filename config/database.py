from neo4j import GraphDatabase

# Define las conexiones
URI = NEO4J_URI
AUTH = (NEO4J_USERNAME,NEO4J_PASSWORD)

# Crear la instancia driver
driver = GraphDatabase.driver(URI, auth = AUTH)

with driver:
    driver.verify_connectivity()
    print("Connection established.")