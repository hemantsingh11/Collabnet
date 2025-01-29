import json
from neo4j_connection import conn
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = "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"

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def fetch_research_interests():
    """Fetch all research interests from the Neo4j graph."""
    query = """
    MATCH (r:ResearchInterest)
    RETURN r.name AS name
    """
    results = conn.execute_query(query)
    return [row["name"] for row in results]

def get_embedding(text, model="text-embedding-3-small"):
    """Generate embedding for a given text using OpenAI API."""
    try:
        text = text.replace("\n", " ")  # Sanitize input
        response = client.embeddings.create(input=[text], model=model)
        return response.data[0].embedding  # Extract the embedding
    except Exception as e:
        print(f"Error generating embedding for '{text}': {e}")
        return None

def generate_and_store_embeddings():
    """Generate embeddings for research interests and store them in Neo4j."""
    research_interests = fetch_research_interests()
    print(f"Generating embeddings for {len(research_interests)} research interests...")

    for interest in research_interests:
        # Generate embedding using OpenAI
        embedding = get_embedding(interest)
        if embedding:
            # Store embedding in Neo4j
            query = """
            MATCH (r:ResearchInterest {name: $name})
            SET r.embedding = $embedding
            """
            conn.execute_query(query, {"name": interest, "embedding": json.dumps(embedding)})
            print(f"Stored embedding for: {interest}")
        else:
            print(f"Skipping embedding for: {interest}")

    print("Embeddings generated and stored successfully!")

if __name__ == "__main__":
    generate_and_store_embeddings()
