from neo4j_connection import conn

def get_community_id(faculty_name):
    """Fetch the community ID for the given faculty name."""
    query = """
    MATCH (f:Faculty {name: $faculty_name})
    RETURN f.communityId AS communityId
    """
    result = conn.execute_query(query, {"faculty_name": faculty_name})
    return result[0]['communityId'] if result else None

def get_faculty_in_community(community_id):
    """Retrieve faculty members in a specific community."""
    query = """
    MATCH (f:Faculty)
    WHERE f.communityId = $community_id
    RETURN f.name AS Name, f.position AS Position, 
           f.department AS Department, f.school AS School, 
           f.fullProfileLink AS ProfileLink
    ORDER BY f.name
    """
    return conn.execute_query(query, {"community_id": community_id})

def get_top_collaborations(community_id):
    """Retrieve strongest collaborations within the community."""
    query = """
    MATCH (f1:Faculty)-[c:COLLABORATES_WITH]-(f2:Faculty)
    WHERE f1.communityId = f2.communityId AND f1.communityId = $community_id
    RETURN f1.name AS Faculty1, f2.name AS Faculty2, 
           c.coAuthoredPublications AS Publications
    ORDER BY Publications DESC
    LIMIT 10
    """
    return conn.execute_query(query, {"community_id": community_id})

def get_top_research_interests(community_id):
    """Find the most common research interests in the community."""
    query = """
    MATCH (f:Faculty)-[:HAS_INTEREST]-(r:ResearchInterest)
    WHERE f.communityId = $community_id
    RETURN r.name AS ResearchInterest, COUNT(f) AS InterestCount
    ORDER BY InterestCount DESC
    LIMIT 10
    """
    return conn.execute_query(query, {"community_id": community_id})

if __name__ == "__main__":
    faculty_name = "Huimin Cheng"
    print(f"Finding community for {faculty_name}...")

    community_id = get_community_id(faculty_name)
    if community_id is None:
        print(f"No community found for {faculty_name}.")
    else:
        print(f"{faculty_name} is in Community ID: {community_id}")

        print("\n--- Faculty Members in Community ---")
        faculty_list = get_faculty_in_community(community_id)
        for faculty in faculty_list:
            print(f"{faculty['Name']} | {faculty['Position']} | {faculty['Department']} | {faculty['School']} | {faculty['ProfileLink']}")

        print("\n--- Top Collaborations in Community ---")
        collaborations = get_top_collaborations(community_id)
        for collab in collaborations:
            print(f"{collab['Faculty1']} - {collab['Faculty2']}: {collab['Publications']} co-authored papers")

        print("\n--- Top Research Interests in Community ---")
        research_interests = get_top_research_interests(community_id)
        for interest in research_interests:
            print(f"{interest['ResearchInterest']} (shared by {interest['InterestCount']} faculty)")
