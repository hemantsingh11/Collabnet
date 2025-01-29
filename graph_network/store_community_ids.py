from neo4j_connection import conn

def drop_existing_graph():
    """Drops the existing graph projection if it exists."""
    print("Checking for existing graph projection...")
    query = """
    CALL gds.graph.exists('facultyCollaborationGraph') 
    YIELD exists 
    RETURN exists
    """
    result = conn.execute_query(query)
    
    if result and result[0]['exists']:
        print("Graph exists. Dropping it...")
        conn.execute_query("CALL gds.graph.drop('facultyCollaborationGraph')")
        print("Graph dropped successfully.")
    else:
        print("No existing graph found. Proceeding with projection.")

def project_graph():
    """Projects the graph in Neo4j if not already projected."""
    print("Projecting the graph...")
    query = """
    CALL gds.graph.project(
        'facultyCollaborationGraph',
        'Faculty',
        {
            COLLABORATES_WITH: {
                type: 'COLLABORATES_WITH',
                properties: 'coAuthoredPublications'
            }
        }
    )
    """
    conn.execute_query(query)
    print("Graph projection completed.")

def store_community_ids():
    """Runs Louvain at resolution 0.5 and stores community IDs in Neo4j."""
    print("Running Louvain community detection at resolution 0.5...")

    query = """
    CALL gds.louvain.write('facultyCollaborationGraph', {
        relationshipWeightProperty: 'coAuthoredPublications',
        tolerance: 0.0001,
        maxIterations: 20,
        writeProperty: 'communityId'
    })
    YIELD communityCount, modularity
    RETURN communityCount, modularity
    """

    result = conn.execute_query(query)
    print("\n--- Community Detection Results ---")
    print(f"Total Communities: {result[0]['communityCount']}")
    print(f"Modularity Score: {result[0]['modularity']}")
    print("Community IDs stored successfully!")

if __name__ == "__main__":
    try:
        # Step 1: Drop existing graph if needed
        drop_existing_graph()

        # Step 2: Project the graph
        project_graph()

        # Step 3: Run Louvain and store community IDs
        store_community_ids()

    except Exception as e:
        print(f"An error occurred: {e}")
