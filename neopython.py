from neo4j import GraphDatabase

# Replace with your Neo4j database URI, username, and password
uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "your_password"))

def create_person(tx, name):
    result = tx.run("CREATE (p:Person {name: $name}) RETURN p", name=name)
    for record in result:
        print(f"Created person: {record['p']}")

with driver.session() as session:
    session.write_transaction(create_person, "Alice")
