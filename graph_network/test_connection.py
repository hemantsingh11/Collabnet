from neo4j import GraphDatabase

# Local Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "collabnet"

# Create a driver object
driver = GraphDatabase.driver(uri, auth=(username, password))

# Verify the connection
with driver.session() as session:
    session.run("MATCH (n) RETURN n LIMIT 1")
    print("Connection successful!")

# Close the driver when done
driver.close()
