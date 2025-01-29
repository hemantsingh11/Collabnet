from neo4j import GraphDatabase

# Replace with your actual Neo4j connection details
uri = "neo4j+ssc://6fcd308f.databases.neo4j.io"
username = "neo4j"
password = "B0TLjzO5C5GWXOpLpVSXGCy-9Wo5FgAJ6fCxMfPe0z8"

# Create a driver object
driver = GraphDatabase.driver(uri, auth=(username, password))

# Verify the connection
with driver.session() as session:
    session.run("MATCH (n) RETURN n LIMIT 1")
    print("Connection successful!")

# Close the driver when done
driver.close()