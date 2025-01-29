import json
import os
from utils.coauthor_expansion import update_json_with_profile
from utils.concepts_extractor import process_research_interests
from utils.co_author_extractor import process_co_authors

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):
    """Save JSON data to a file and ensure it's properly written."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            file.flush()  # Ensures data is written to disk
        print(f"Data successfully saved to: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error saving JSON: {e}")

def format_name(name):
    """Format name from 'Last, First' to 'First Last'."""
    parts = name.split(', ')
    return f"{parts[1]} {parts[0]}" if len(parts) == 2 else name

def process_profile(json_file, profile):
    """Extract and update research interests and co-author details for a profile."""
    print(f"Processing profile for: {profile['name']}")

    # Process research interests
    research_interests = process_research_interests(profile["full_profile_link"])
    if research_interests:
        profile["research_interest"] = research_interests
        print(f"Research interests found for {profile['name']}: {len(research_interests)} interests.")

    # Process co-authors
    co_author_details = process_co_authors(profile["full_profile_link"])
    if co_author_details:
        profile["co_author_details"] = co_author_details
        print(f"Co-author details extracted successfully for {profile['name']}.")

def process_co_authors_of_selected_profile(json_file, selected_name, co_author_limit):
    """Process only the co-authors of the given profile and extract their details sequentially, skipping already processed profiles."""
    data = load_json(json_file)

    # Find the selected profile (Salma Mohamed Hassan Abdalla)
    profile = next((p for p in data if p["name"] == selected_name), None)

    if not profile:
        print(f"Profile for {selected_name} not found.")
        return

    print(f"Fetching co-authors of: {selected_name}")

    co_authors = profile.get("co_author_details", {}).get("Co-Authors", [])[:co_author_limit]

    for author in co_authors:
        name = format_name(author["Name"]["value"])
        profile_link = author["Name"]["link"]

        # Check if the co-author is already processed
        existing_profile = next((p for p in data if p["name"] == name), None)

        if existing_profile and existing_profile.get("research_interest") and existing_profile.get("co_author_details"):
            print(f"Skipping already processed co-author: {name}")
            continue  # Skip to the next co-author

        print(f"\n--- Processing co-author: {name} ---")

        # Step 1: Update profile data
        updated_data = update_json_with_profile(json_file, name, profile_link)
        if updated_data:
            save_json(json_file, updated_data)
            print(f"{name} profile saved successfully.")

            # Reload JSON to ensure persistence
            data = load_json(json_file)

        # Step 2: Process research interests and co-author details together
        new_profile = next((p for p in data if p["name"] == name), None)
        if new_profile:
            print(f"Processing research interests and co-authors for: {name}")

            # Fetch research interests
            research_interests = process_research_interests(new_profile["full_profile_link"])
            if research_interests:
                new_profile["research_interest"] = research_interests
                print(f"Research interests found for {name}: {len(research_interests)}")

            # Fetch co-author details
            co_author_details = process_co_authors(new_profile["full_profile_link"])
            if co_author_details:
                new_profile["co_author_details"] = co_author_details
                print(f"Co-author details extracted successfully for {name}.")

            # Save updated profile after processing both research interests and co-authors
            save_json(json_file, data)
            print(f"{name}'s profile fully updated in JSON.")

    print(f"\nSuccessfully updated the JSON file with co-authors and research interests of {selected_name}.")


if __name__ == "__main__":
    # Specify the main profile and number of co-authors to process
    selected_name = "Salma Mohamed Hassan Abdalla"
    co_author_limit = 5  # Change this number to process more or fewer co-authors
    
    process_co_authors_of_selected_profile("final_data1.json", selected_name, co_author_limit)
