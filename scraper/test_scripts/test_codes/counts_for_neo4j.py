import json
from collections import Counter

def analyze_data(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)

    # Count total faculty
    total_faculty = len(data)

    # Collect all research interests
    research_interests = []
    co_author_counts = []
    co_author_of_co_authors_counts = []
    co_author_connections_counts = []

    for faculty in data:
        # Add research interests
        if "research_interest" in faculty:
            research_interests.extend(faculty["research_interest"])

        # Count co-authors
        if "co_author_details" in faculty and "Co-Authors" in faculty["co_author_details"]:
            co_author_counts.append(len(faculty["co_author_details"]["Co-Authors"]))

        # Count co-authors of co-authors
        if "co_author_details" in faculty and "Co-Authors of Co-Authors" in faculty["co_author_details"]:
            co_author_of_co_authors_counts.append(len(faculty["co_author_details"]["Co-Authors of Co-Authors"]))

        # Count co-author connections
        if "co_author_details" in faculty and "Co-Author Connections" in faculty["co_author_details"]:
            co_author_connections_counts.append(len(faculty["co_author_details"]["Co-Author Connections"]))

    # Calculate unique research interests
    unique_research_interests = set(research_interests)

    # Get statistics
    stats = {
        "Total Faculty": total_faculty,
        "Total Research Interests": len(research_interests),
        "Unique Research Interests": len(unique_research_interests),
        "Max Co-Authors per Faculty": max(co_author_counts, default=0),
        "Max Co-Authors of Co-Authors per Faculty": max(co_author_of_co_authors_counts, default=0),
        "Max Co-Author Connections per Faculty": max(co_author_connections_counts, default=0),
        "Average Co-Authors per Faculty": sum(co_author_counts) / total_faculty if total_faculty > 0 else 0,
        "Average Co-Authors of Co-Authors per Faculty": sum(co_author_of_co_authors_counts) / total_faculty if total_faculty > 0 else 0,
        "Average Co-Author Connections per Faculty": sum(co_author_connections_counts) / total_faculty if total_faculty > 0 else 0,
    }

    return stats, unique_research_interests

# Example usage
json_file = "final_data1 copy.json"  # Replace with your JSON file path
stats, unique_research_interests = analyze_data(json_file)

# Display results
print("=== Analysis Results ===")
for key, value in stats.items():
    print(f"{key}: {value}")

print("\nSample Unique Research Interests:")
print(list(unique_research_interests)[:10])  # Show a sample of unique research interests
