from neo4j_connection import conn

def get_top_degree_centrality(limit=5):
    """Retrieve top faculty by degree centrality."""
    query = """
    MATCH (f:Faculty)
    RETURN f.name AS Faculty, f.degreeCentrality AS DegreeCentrality
    ORDER BY DegreeCentrality DESC
    LIMIT $limit
    """
    return conn.execute_query(query, {"limit": limit})

def get_top_betweenness_centrality(limit=5):
    """Retrieve top faculty by betweenness centrality."""
    query = """
    MATCH (f:Faculty)
    RETURN f.name AS Faculty, f.betweennessCentrality AS BetweennessCentrality
    ORDER BY BetweennessCentrality DESC
    LIMIT $limit
    """
    return conn.execute_query(query, {"limit": limit})

def get_top_closeness_centrality(limit=5):
    """Retrieve top faculty by closeness centrality."""
    query = """
    MATCH (f:Faculty)
    RETURN f.name AS Faculty, f.closenessCentrality AS ClosenessCentrality
    ORDER BY ClosenessCentrality DESC
    LIMIT $limit
    """
    return conn.execute_query(query, {"limit": limit})

def analyze_department_collaborations():
    """Analyze collaboration extent by department."""
    query = """
    MATCH (f:Faculty)
    RETURN f.department AS Department, COUNT(f) AS FacultyCount, 
           avg(f.degreeCentrality) AS AvgDegree, 
           avg(f.betweennessCentrality) AS AvgBetweenness, 
           avg(f.closenessCentrality) AS AvgCloseness
    ORDER BY FacultyCount DESC
    """
    return conn.execute_query(query)

if __name__ == "__main__":
    print("\n--- Degree Centrality ---")
    for row in get_top_degree_centrality():
        print(f"Faculty: {row['Faculty']}, Degree: {row['DegreeCentrality']}")

    print("\n--- Betweenness Centrality ---")
    for row in get_top_betweenness_centrality():
        print(f"Faculty: {row['Faculty']}, Betweenness: {row['BetweennessCentrality']}")

    print("\n--- Closeness Centrality ---")
    for row in get_top_closeness_centrality():
        print(f"Faculty: {row['Faculty']}, Closeness: {row['ClosenessCentrality']}")

    print("\n--- Department-Level Collaboration Analysis ---")
    for row in analyze_department_collaborations():
        print(f"Department: {row['Department']}, FacultyCount: {row['FacultyCount']}, "
              f"AvgDegree: {row['AvgDegree']:.2f}, AvgBetweenness: {row['AvgBetweenness']:.2f}, "
              f"AvgCloseness: {row['AvgCloseness']:.2f}")
