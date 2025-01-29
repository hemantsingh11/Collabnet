import collaboration_analysis as analysis

def generate_report():
    """Generates a detailed report for tasks 2, 3, and 4."""
    print("Generating Report...\n")

    # Task 2: Analyze Network Structure
    print("--- Task 2: Analyze Network Structure ---")
    try:
        # Fetch collaboration by department and print results
        collaboration_by_department = analysis.analyze_collaboration_by_attribute("department")
        analysis.print_analysis_results("Collaboration by Department", collaboration_by_department)

        # Fetch collaboration by school and print results
        collaboration_by_school = analysis.analyze_collaboration_by_attribute("school")
        analysis.print_analysis_results("Collaboration by School", collaboration_by_school)
    except Exception as e:
        print(f"Error analyzing network structure: {e}")

    # Task 3: Determine Influential Factors
    print("\n--- Task 3: Determine Influential Factors ---")
    try:
        # Fetch and print research interest overlap
        research_interest_overlap = analysis.analyze_research_interest_overlap()
        analysis.print_analysis_results("Research Interest Overlap", research_interest_overlap)
    except Exception as e:
        print(f"Error determining influential factors: {e}")

    # Task 4: Community Detection
    print("\n--- Task 4: Community Detection ---")
    try:
        # Fetch precomputed community data
        query = """
        MATCH (f:Faculty)
        RETURN f.communityId AS communityId, count(f) AS memberCount
        ORDER BY memberCount DESC
        """
        community_results = analysis.conn.execute_query(query)
        analysis.print_analysis_results("Community Detection Results", community_results)
    except Exception as e:
        print(f"Error in community detection analysis: {e}")

    print("\nReport generation completed.")

if __name__ == "__main__":
    generate_report()
