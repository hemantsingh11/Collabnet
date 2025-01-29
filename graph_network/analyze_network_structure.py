from neo4j_connection import conn

# Analysis functions
def analyze_network_structure(conn):
    try:
        # 1. Total nodes and relationships
        print("Analyzing graph structure...")
        summary_query = """
        MATCH (n)-[r]->(m)
        RETURN COUNT(DISTINCT n) AS totalNodes, COUNT(r) AS totalRelationships;
        """
        summary = conn.execute_query(summary_query)
        total_nodes = summary[0]['totalNodes']
        total_relationships = summary[0]['totalRelationships']

        # 2. Degree centrality (how connected each node is)
        centrality_query = """
        MATCH (n)-[r]->()
        RETURN n.name AS facultyName, COUNT(r) AS degreeCentrality
        ORDER BY degreeCentrality DESC
        LIMIT 5;
        """
        degree_centrality = conn.execute_query(centrality_query)

        # 3. Detect clusters (community detection using label propagation)
        # Step 3.1: Project the graph for GDS
        project_query = """
        CALL gds.graph.project(
          'collaborationGraph',
          'Faculty',
          {
            COLLABORATES_WITH: {
              properties: 'coAuthoredPublications'
            }
          }
        )
        """
        conn.execute_query(project_query)

        # Step 3.2: Run label propagation
        cluster_query = """
        CALL gds.labelPropagation.stream('collaborationGraph')
        YIELD nodeId, communityId
        RETURN gds.util.asNode(nodeId).name AS facultyName, communityId
        ORDER BY communityId;
        """
        clusters = conn.execute_query(cluster_query)

        # 4. Print meaningful summaries
        print("\n--- Graph Summary ---")
        print(f"Total Nodes: {total_nodes}")
        print(f"Total Relationships: {total_relationships}")

        print("\n--- Top 5 Faculty by Degree Centrality ---")
        for row in degree_centrality:
            print(f"Faculty: {row['facultyName']}, Degree Centrality: {row['degreeCentrality']}")

        print("\n--- Detected Clusters ---")
        cluster_dict = {}
        for row in clusters:
            community_id = row['communityId']
            faculty_name = row['facultyName']
            cluster_dict.setdefault(community_id, []).append(faculty_name)

        for community_id, members in cluster_dict.items():
            print(f"Community {community_id}: {', '.join(members[:5])}...")  # Print first 5 members per cluster

    except Exception as e:
        print(f"An error occurred during network analysis: {e}")

# Main script
if __name__ == "__main__":
    analyze_network_structure(conn)
