import json
import time
from tqdm import tqdm  # Progress bar library
from neo4j_connection import conn

def normalize_name(name):
    """Convert 'Last, First' format to 'First Last'."""
    parts = name.split(", ")
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

def load_data_to_neo4j(json_file):
    # Load the JSON file
    print("Loading data from JSON...")
    with open(json_file, "r") as file:
        faculty_data = json.load(file)

    total_faculty = len(faculty_data)
    print(f"Loaded {total_faculty} faculty records.")

    # Start data ingestion with a progress bar
    print("Starting data ingestion into Neo4j...")
    start_time = time.time()
    faculty_names = {faculty["name"] for faculty in faculty_data}  # All valid faculty names

    for i, faculty in enumerate(tqdm(faculty_data, desc="Processing Faculty", unit="faculty")):
        faculty_name = faculty["name"]

        # Step 1: Create Faculty Node
        query = """
        MERGE (f:Faculty {
            name: $name,
            position: $position,
            department: $department,
            school: $school,
            email: $email,
            profileLink: $profileLink,
            fullProfileLink: $fullProfileLink
        })
        """
        conn.execute_query(query, {
            "name": faculty_name,
            "position": faculty["position"],
            "department": faculty["department"],
            "school": faculty["school"],  # Directly using the 'school' attribute
            "email": faculty["email"],
            "profileLink": faculty["profile_link"],
            "fullProfileLink": faculty["full_profile_link"]
        })

        # Step 2: Handle Research Interests
        if "research_interest" in faculty and faculty["research_interest"]:
            for interest in faculty["research_interest"]:
                query = """
                MERGE (r:ResearchInterest {name: $interest})
                MERGE (f:Faculty {name: $faculty_name})
                MERGE (f)-[:HAS_INTEREST]-(r)  // Undirected relationship
                """
                conn.execute_query(query, {
                    "interest": interest,
                    "faculty_name": faculty_name
                })

        # Step 3: Handle Co-Authors
        if "co_author_details" in faculty and "Co-Authors" in faculty["co_author_details"]:
            for coauthor in faculty["co_author_details"]["Co-Authors"]:
                coauthor_name = normalize_name(coauthor["Name"]["value"])

                if coauthor_name in faculty_names:
                    # Create COLLABORATES_WITH relationship as undirected
                    query = """
                    MATCH (f1:Faculty {name: $faculty_name})
                    MATCH (f2:Faculty {name: $coauthor_name})
                    MERGE (f1)-[c:COLLABORATES_WITH]-(f2)
                    ON CREATE SET
                        c.coAuthoredPublications = toInteger($coAuthoredPublications)
                    """
                    conn.execute_query(query, {
                        "faculty_name": faculty_name,
                        "coauthor_name": coauthor_name,
                        "coAuthoredPublications": coauthor["Co-Authored Publications"]["value"]
                    })
                else:
                    # Add missing co-author as metadata
                    query = """
                    MATCH (f:Faculty {name: $faculty_name})
                    SET f.missingCoAuthors = coalesce(f.missingCoAuthors, []) + $coauthor_name
                    """
                    conn.execute_query(query, {
                        "faculty_name": faculty_name,
                        "coauthor_name": coauthor_name
                    })

        # Step 4: Handle Co-Authors of Co-Authors
        if "co_author_details" in faculty and "Co-Authors of Co-Authors" in faculty["co_author_details"]:
            for coauthor in faculty["co_author_details"]["Co-Authors of Co-Authors"]:
                coauthor_name = normalize_name(coauthor["Name"]["value"])
                # Add missing co-authors of co-authors as metadata
                query = """
                MATCH (f:Faculty {name: $faculty_name})
                SET f.missingCoAuthorsOfCoAuthors = coalesce(f.missingCoAuthorsOfCoAuthors, []) + $coauthor_name
                """
                conn.execute_query(query, {
                    "faculty_name": faculty_name,
                    "coauthor_name": coauthor_name
                })

        # Step 5: Handle Co-Author Connections
        if "co_author_details" in faculty and "Co-Author Connections" in faculty["co_author_details"]:
            for connection in faculty["co_author_details"]["Co-Author Connections"]:
                person1 = normalize_name(connection["Person 1"]["value"])
                person2 = normalize_name(connection["Person 2"]["value"])
                if person1 not in faculty_names or person2 not in faculty_names:
                    # Add missing connections as metadata
                    query = """
                    MATCH (f:Faculty {name: $faculty_name})
                    SET f.missingCoAuthorConnections = coalesce(f.missingCoAuthorConnections, []) + $connection
                    """
                    conn.execute_query(query, {
                        "faculty_name": faculty_name,
                        "connection": f"{person1} - {person2}"
                    })

        # Update the progress bar description with time remaining
        elapsed_time = time.time() - start_time
        avg_time_per_faculty = elapsed_time / (i + 1)
        time_remaining = avg_time_per_faculty * (total_faculty - (i + 1))
        tqdm.write(f"Estimated time remaining: {time_remaining // 60:.0f} min {time_remaining % 60:.0f} sec", end="\r")

    print("\nData ingestion completed successfully!")

# Run the script
if __name__ == "__main__":
    json_file = "final_data.json"  # Replace with the path to your JSON file
    load_data_to_neo4j(json_file)
