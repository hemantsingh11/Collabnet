from neo4j_connection import conn

def get_top_communities(limit=5):
    """Retrieve the largest communities and their sizes."""
    query = """
    MATCH (f:Faculty)
    RETURN f.communityId AS Community, COUNT(f) AS MemberCount
    ORDER BY MemberCount DESC
    LIMIT $limit
    """
    return conn.execute_query(query, {"limit": limit})

def get_community_details(community_id):
    """Retrieve faculty details from a specific community."""
    query = """
    MATCH (f:Faculty)
    WHERE f.communityId = $community_id
    RETURN f.name AS Faculty, f.degreeCentrality AS Degree, f.betweennessCentrality AS Betweenness,
           f.closenessCentrality AS Closeness, f.eigenvectorCentrality AS Eigenvector
    ORDER BY Degree DESC
    """
    return conn.execute_query(query, {"community_id": community_id})

if __name__ == "__main__":
    print("\n--- Top Communities ---")
    communities = get_top_communities()
    for row in communities:
        print(f"Community {row['Community']}: {row['MemberCount']} members")

    # Fetch details for the largest community
    if communities:
        largest_community_id = communities[0]['Community']
        print(f"\n--- Details for Largest Community (ID: {largest_community_id}) ---")
        members = get_community_details(largest_community_id)
        for row in members[:10]:  # Show top 10 members only
            print(f"Faculty: {row['Faculty']}, Degree: {row['Degree']}, "
                  f"Betweenness: {row['Betweenness']}, Closeness: {row['Closeness']}, "
                  f"Eigenvector: {row['Eigenvector']}")
