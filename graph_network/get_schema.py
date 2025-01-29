from neo4j_connection import conn

def list_all_gds_graphs():
    """Lists all projected graphs inside Neo4j GDS."""
    print("\nFetching list of projected graphs...\n")

    query = """
    CALL gds.graph.list()
    YIELD graphName, nodeCount, relationshipCount, schema
    RETURN graphName, nodeCount, relationshipCount, schema
    """
    
    results = conn.execute_query(query)

    if not results:
        print("No projected graphs found in GDS.")
        return []

    print("--- Projected Graphs in GDS ---")
    for row in results:
        print(f"Graph Name: {row['graphName']}")
        print(f"  Nodes: {row['nodeCount']}")
        print(f"  Relationships: {row['relationshipCount']}")
        print(f"  Schema: {row['schema']}\n")
    
    return [row['graphName'] for row in results]  # Returns list of graph names

def get_graph_schema(graph_name):
    """Fetches schema details for a specific GDS-projected graph."""
    print(f"\nFetching schema for graph: {graph_name}...\n")

    query = f"""
    CALL gds.graph.list()
    YIELD graphName, schema
    WHERE graphName = '{graph_name}'
    RETURN schema
    """

    results = conn.execute_query(query)

    if results:
        print(f"--- Schema for {graph_name} ---")
        print(results[0]['schema'])
    else:
        print(f"No projected graph found with name: {graph_name}")

# Run functions
graph_names = list_all_gds_graphs()
if graph_names:
    for g_name in graph_names:
        get_graph_schema(g_name)
