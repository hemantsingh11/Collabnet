import matplotlib.pyplot as plt
from neo4j_connection import conn

def project_graph():
    """Projects the graph in Neo4j for community detection."""
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

def run_louvain_with_parameters(resolutions):
    """Run Louvain with varying parameters and collect results."""
    print("Running Louvain with varying resolutions...")
    results = []
    for resolution in resolutions:
        print(f"Running for resolution: {resolution}")
        query = f"""
        CALL gds.louvain.stream('facultyCollaborationGraph', {{
            relationshipWeightProperty: 'coAuthoredPublications',
            tolerance: 0.0001,
            maxIterations: 20
        }})
        YIELD nodeId, communityId
        RETURN communityId AS communityId, count(nodeId) AS communitySize
        """
        result = conn.execute_query(query)
        for row in result:
            results.append({
                "resolution": resolution,
                "communityId": row["communityId"],
                "communitySize": row["communitySize"]
            })
    return results

def cleanup_projection():
    """Deletes the projected graph from Neo4j."""
    print("Deleting projected graph...")
    query = "CALL gds.graph.drop('facultyCollaborationGraph')"
    conn.execute_query(query)
    print("Graph deleted successfully.")

def plot_results(results):
    """Plot modularity vs. resolution to find the elbow point."""
    resolutions = [res['resolution'] for res in results]
    sizes = [res['communitySize'] for res in results]

    plt.plot(resolutions, sizes, marker='o')
    plt.title("Community Size vs Resolution")
    plt.xlabel("Resolution")
    plt.ylabel("Community Size")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    try:
        # Step 1: Project the graph
        project_graph()

        # Step 2: Run Louvain with varying resolutions
        resolutions = [0.1, 0.3, 0.5, 0.7, 1.0]  # Adjust as needed
        results = run_louvain_with_parameters(resolutions)

        # Step 3: Display results
        print("\n--- Results ---")
        for res in results:
            print(f"Resolution: {res['resolution']}, Community ID: {res['communityId']}, Community Size: {res['communitySize']}")

        # Step 4: Plot results to find the elbow point
        plot_results(results)

    finally:
        # Step 5: Clean up the graph projection
        cleanup_projection()
