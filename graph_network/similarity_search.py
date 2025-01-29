import numpy as np
import json
from neo4j_connection import conn

def find_similar_research_interests(target_interest, top_n=5):
    """Find similar research interests based on vector embeddings."""
    # Fetch the embedding for the target research interest
    query = """
    MATCH (r:ResearchInterest {name: $name})
    RETURN r.embedding AS embedding
    """
    result = conn.execute_query(query, {"name": target_interest})
    if not result:
        print(f"Research interest '{target_interest}' not found.")
        return []

    target_embedding = np.array(json.loads(result[0]["embedding"]))

    # Fetch embeddings for all other research interests
    query = """
    MATCH (r:ResearchInterest)
    WHERE r.name <> $target_name
    RETURN r.name AS name, r.embedding AS embedding
    """
    results = conn.execute_query(query, {"target_name": target_interest})

    # Calculate cosine similarity
    similarities = []
    for row in results:
        name = row["name"]
        embedding = np.array(json.loads(row["embedding"]))
        similarity = np.dot(target_embedding, embedding) / (
            np.linalg.norm(target_embedding) * np.linalg.norm(embedding)
        )
        similarities.append((name, similarity))

    # Sort by similarity
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]
    return similarities

def recommend_faculty_by_interest(target_interest, top_n=5):
    """Recommend faculty based on similar research interests."""
    similar_interests = find_similar_research_interests(target_interest, top_n)
    if not similar_interests:
        return []

    # Fetch faculty linked to similar research interests
    interest_names = [name for name, _ in similar_interests]
    query = """
    MATCH (f:Faculty)-[:HAS_INTEREST]-(r:ResearchInterest)
    WHERE r.name IN $interest_names
    RETURN f.name AS faculty_name, f.position AS position, f.department AS department,
           f.school AS school, f.fullProfileLink AS full_profile_link, r.name AS research_interest
    """
    # Pass both the query and the parameters
    results = conn.execute_query(query, {"interest_names": interest_names})

    # Organize results
    recommendations = {}
    for row in results:
        interest = row["research_interest"]
        faculty_details = {
            "name": row["faculty_name"],
            "position": row["position"],
            "department": row["department"],
            "school": row["school"],
            "full_profile_link": row["full_profile_link"],
        }
        recommendations.setdefault(interest, []).append(faculty_details)

    return recommendations

if __name__ == "__main__":
    target = "Global Health"  # Replace with your target research interest
    print(f"Finding similar research interests to '{target}'...\n")
    recommendations = recommend_faculty_by_interest(target)

    if recommendations:
        print("Recommended Faculty:")
        for interest, faculty_list in recommendations.items():
            print(f"\nInterest: {interest}")
            for faculty in faculty_list:
                print(f"  - {faculty['name']} ({faculty['position']}, {faculty['department']}, {faculty['school']})")
                print(f"    Full Profile: {faculty['full_profile_link']}")
                print()
    else:
        print("No recommendations found.")