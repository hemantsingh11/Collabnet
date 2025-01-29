from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password, verbose=False):
        print("Initializing connection to Neo4j...")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.verbose = verbose
        print("Connection initialized successfully.")

    def close(self):
        print("Closing connection to Neo4j...")
        self.driver.close()
        print("Connection closed.")

    def execute_query(self, query, parameters=None):
        if self.verbose:
            print("Executing query on Neo4j...")
            if parameters:
                print(f"Query Parameters: {parameters}")
        with self.driver.session() as session:
            result = session.run(query, parameters)
            if self.verbose:
                print("Query executed successfully.")
            return result.data()  # Fetch all results as a list of dictionaries


# Update the following with your local Neo4j instance details
URI = "bolt://localhost:7687"  # Default local Neo4j URI
USERNAME = "neo4j"  # Default username
PASSWORD = "collabnet"  # Replace with your local Neo4j password

# Set verbose to True for debugging or False for cleaner output
conn = Neo4jConnection(URI, USERNAME, PASSWORD, verbose=False)
