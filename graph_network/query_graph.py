from neo4j_connection import conn

# Query for co-authors with specific research interests
def get_coauthors_with_interest(faculty_name, interest_name):
    print(f"Executing query to find co-authors of '{faculty_name}' with interest '{interest_name}'...")
    query = """
    MATCH (f:Faculty {name: $faculty_name})-[:COLLABORATES_WITH]->(coauthor)-[:HAS_INTEREST]->(interest)
    WHERE interest.name = $interest_name
    RETURN coauthor.name AS CoAuthor, interest.name AS Interest
    """
    result = conn.execute_query(query, {
        "faculty_name": faculty_name,
        "interest_name": interest_name
    })
    print(f"Query completed. Found {len(result)} co-author(s) with interest '{interest_name}'.")
    return result

# List of research interests
terms = [
    "Public Health"
]

# Faculty name to search co-authors for
faculty_name = "Salma Mohamed Hassan Abdalla"

# Loop through all research interests
for interest_name in terms:
    print(f"\nRunning query for faculty '{faculty_name}' and interest '{interest_name}'...")
    result = get_coauthors_with_interest(faculty_name, interest_name)
    
    # Display the results
    if result:
        print("Co-authors with matching research interest:")
        for record in result:
            print(f"  - Co-Author: {record['CoAuthor']}, Interest: {record['Interest']}")
    else:
        print(f"No co-authors found for faculty '{faculty_name}' with interest '{interest_name}'.")
