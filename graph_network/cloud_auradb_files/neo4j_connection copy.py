from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

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

# Use environment variables
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

# Set verbose to False for cleaner output
conn = Neo4jConnection(URI, USERNAME, PASSWORD, verbose=False)
