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

#if you want to make more complex query, you can try with this:
def find_friends(tx, person_name):
    result = tx.run("""
        MATCH (p:Person {name: $name})-[:KNOWS]->(friend)
        RETURN friend.name AS friend_name
    """, name=person_name)
    for record in result:
        print(f"Friend of {person_name}: {record['friend_name']}")
