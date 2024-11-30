from cassandra.cluster import Cluster
import uuid


cluster = Cluster(['127.0.0.1']) 
session = cluster.connect()


session.execute("""
CREATE KEYSPACE IF NOT EXISTS test_keyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")

session.set_keyspace('test_keyspace')
# create table
session.execute("""
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INT
)
""")

add data
session.execute("""
INSERT INTO users (id, name, email, age) VALUES (%s, %s, %s, %s)
""", (uuid.uuid4(), 'John Doe', 'john@example.com', 30))
