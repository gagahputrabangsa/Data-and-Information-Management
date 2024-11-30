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

rows = session.execute("SELECT * FROM users")
for row in rows:
    print(f"ID: {row.id}, Name: {row.name}, Email: {row.email}, Age: {row.age}")


row = session.execute("SELECT * FROM users WHERE id=%s", [some_uuid]).one()
if row:
    print(f"Name: {row.name}, Email: {row.email}")
else:
    print("User not found")
