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

