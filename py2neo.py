from py2neo import Graph

# Conn
graph = Graph("bolt://localhost:7687", auth=("neo4j", "ur_pass"))

