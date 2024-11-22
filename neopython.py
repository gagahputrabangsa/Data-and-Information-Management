from neo4j import GraphDatabase

# Replace with your Neo4j database URI, username, and password
uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "your_password"))
