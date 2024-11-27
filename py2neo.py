from py2neo import Graph

# Conn
graph = Graph("bolt://localhost:7687", auth=("neo4j", "ur_pass"))

# Create
graph.run("CREATE (p:Person {name: 'Reza', age: 18})")
graph.run("CREATE (p:Person {name: 'Afni', age: 27})")
graph.run("CREATE (p:Person {name: 'Agfan', age: 20})")
graph.run("CREATE (p:Person {name: 'Arief', age: 25})")
graph.run("CREATE (p:Person {name: 'Made', age: 31})")
print("Node created!")

# Read node (Person)
nodes = graph.run("MATCH (p:Person) RETURN p.name AS name, p.age AS age").data()

# Showing result
for node in nodes:
    print(f"Name: {node['name']}, Age: {node['age']}")

# Mengupdate properti node
graph.run("MATCH (p:Person {name: 'Gaga'}) SET p.age = 32")
print("Node berhasil diperbarui!")

#delete
graph.run("MATCH (p:Person {name: 'Reza'}) DELETE p")
print("Node berhasil dihapus!")


#twi way relation

graph.run("""
    MATCH (a:Person {name: 'Gaga'}), (b:Person {name: 'Afni'})
    CREATE (a)-[:FRIEND]->(b), (b)-[:FRIEND]->(a)
""")
print("Relasi dua arah 'friend' berhasil dibuat")
