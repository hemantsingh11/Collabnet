from neo4j_connection import conn

def project_graph():
    """Projects the graph in Neo4j for network analysis."""
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

def compute_centrality_measures():
    """Computes centrality measures for nodes in the graph."""
    print("Computing degree centrality...")
    conn.execute_query("""
    CALL gds.degree.write('facultyCollaborationGraph', {
        writeProperty: 'degreeCentrality'
    })
    """)

    print("Computing betweenness centrality...")
    conn.execute_query("""
    CALL gds.betweenness.write('facultyCollaborationGraph', {
        writeProperty: 'betweennessCentrality'
    })
    """)

    print("Computing closeness centrality...")
    conn.execute_query("""
    CALL gds.closeness.write('facultyCollaborationGraph', {
        writeProperty: 'closenessCentrality'
    })
    """)

    print("Computing eigenvector centrality...")
    conn.execute_query("""
    CALL gds.eigenvector.write('facultyCollaborationGraph', {
        writeProperty: 'eigenvectorCentrality'
    })
    """)

def compute_shortest_path_metrics():
    """Computes shortest path metrics like diameter and average path length."""
    print("Computing all shortest paths...")
    query = """
    CALL gds.allShortestPaths.stream('facultyCollaborationGraph', {
        relationshipWeightProperty: 'coAuthoredPublications'
    })
    YIELD sourceNodeId, targetNodeId, distance
    RETURN max(distance) AS diameter, avg(distance) AS averagePathLength
    """
    return conn.execute_query(query)[0]

def cleanup_projection():
    """Deletes the projected graph from Neo4j."""
    print("Deleting projected graph...")
    query = "CALL gds.graph.drop('facultyCollaborationGraph')"
    conn.execute_query(query)
    print("Graph deleted successfully.")

if __name__ == "__main__":
    try:
        # Step 1: Project the graph
        project_graph()

        # Step 2: Compute centrality measures
        compute_centrality_measures()

        # Step 3: Compute shortest path metrics
        shortest_path_metrics = compute_shortest_path_metrics()

        # Step 4: Print results for the report
        print("\n--- Centrality Analysis ---")
        print("Centrality metrics computed and stored in Neo4j.")

        print("\n--- Graph Metrics ---")
        print(f"Graph Diameter: {shortest_path_metrics['diameter']}")
        print(f"Average Path Length: {shortest_path_metrics['averagePathLength']:.4f}")

    finally:
        # Step 5: Clean up the graph projection
        cleanup_projection()
