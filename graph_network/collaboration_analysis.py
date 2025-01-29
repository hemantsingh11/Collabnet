from neo4j_connection import conn

def analyze_collaboration_by_attribute(attribute):
    """Analyzes the collaboration likelihood and strength by a specific node attribute."""
    print(f"Analyzing collaboration by {attribute}...")
    query = f"""
    MATCH (f:Faculty)-[r:COLLABORATES_WITH]-(f2:Faculty)
    RETURN f.{attribute} AS {attribute},
           count(r) AS collaborationCount,
           avg(r.coAuthoredPublications) AS avgCollaborationStrength,
           sum(r.coAuthoredPublications) AS totalCollaborationStrength
    ORDER BY totalCollaborationStrength DESC
    """
    return conn.execute_query(query)

def analyze_research_interest_overlap():
    """Analyzes how research interest overlap influences collaboration."""
    print("Analyzing research interest overlap...")
    query = """
    MATCH (f1:Faculty)-[:HAS_INTEREST]->(r:ResearchInterest)<-[:HAS_INTEREST]-(f2:Faculty)
    WHERE f1 <> f2
    WITH f1.name AS faculty1, f2.name AS faculty2, collect(r.name) AS sharedInterests
    RETURN faculty1, faculty2, size(sharedInterests) AS sharedInterestCount, sharedInterests
    ORDER BY sharedInterestCount DESC
    LIMIT 10
    """
    return conn.execute_query(query)

def print_analysis_results(title, results):
    """Prints analysis results for the report."""
    print(f"\n--- {title} ---")
    for row in results:
        print(row)

if __name__ == "__main__":
    try:
        # Collaboration by Department
        collaboration_by_department = analyze_collaboration_by_attribute("department")
        print_analysis_results("Collaboration by Department", collaboration_by_department)

        # Collaboration by School
        collaboration_by_school = analyze_collaboration_by_attribute("school")
        print_analysis_results("Collaboration by School", collaboration_by_school)

        # Research Interest Overlap
        research_interest_overlap = analyze_research_interest_overlap()
        print_analysis_results("Research Interest Overlap", research_interest_overlap)

    finally:
        print("Analysis completed.")
