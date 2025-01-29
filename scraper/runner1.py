import json
import os
from utils.email_full_profile_page_extractor import process_profile, save_to_json
from utils.concepts_extractor import process_research_interests
from utils.co_author_extractor import process_co_authors
from utils.common_utils import get_stealth_driver, random_delay

def extract_emails_and_profiles(input_file, driver):
    """Step 1: Extract emails and full profile links for unprocessed profiles."""
    print("Loading profile data from JSON for email extraction...")

    with open(input_file, "r", encoding="utf-8") as file:
        profiles = json.load(file)

    unprocessed_profiles = [profile for profile in profiles if not profile.get("full_profile_link")]

    if not unprocessed_profiles:
        print("All profiles have already been processed for emails and profile links.")
        return

    print(f"Total unprocessed profiles: {len(unprocessed_profiles)}")

    for index, profile in enumerate(unprocessed_profiles, start=1):
        profile_url = profile.get("profile_link")
        if profile_url:
            print(f"\nProcessing profile {index}/{len(unprocessed_profiles)}: {profile_url}")
            profile_info = process_profile(profile_url, driver)
            if profile_info:
                profile["email"] = profile_info.get("email")
                profile["full_profile_link"] = profile_info.get("full_profile_link")
                print(f"Email found: {profile['email']}")
                print(f"Full profile link found: {profile['full_profile_link']}")

    save_to_json(profiles, input_file)

def extract_research_interests(input_file, driver):
    """Step 2: Extract research interests only for profiles where the field is empty."""
    print("\nLoading profile data from JSON for research interests extraction...")

    with open(input_file, "r", encoding="utf-8") as file:
        profiles = json.load(file)

    unprocessed_profiles = [profile for profile in profiles if not profile.get("research_interest")]

    if not unprocessed_profiles:
        print("All profiles have already been processed for research interests.")
        return

    for index, profile in enumerate(unprocessed_profiles, start=1):
        full_profile_link = profile.get("full_profile_link")
        if full_profile_link:
            print(f"\nExtracting research interests for profile {index}/{len(unprocessed_profiles)}: {full_profile_link}")
            research_interests = process_research_interests(full_profile_link, driver)
            if research_interests:
                profile["research_interest"] = research_interests
                print(f"Research interests found: {research_interests}")
            else:
                print("No research interests found.")

    save_to_json(profiles, input_file)

def extract_co_authors(input_file, driver):
    """Step 3: Extract co-author data only for profiles where the field is empty."""
    print("\nLoading profile data from JSON for co-author extraction...")

    with open(input_file, "r", encoding="utf-8") as file:
        profiles = json.load(file)

    unprocessed_profiles = [profile for profile in profiles if not profile.get("co_author_details")]

    if not unprocessed_profiles:
        print("All profiles have already been processed for co-authors.")
        return

    for index, profile in enumerate(unprocessed_profiles, start=1):
        full_profile_link = profile.get("full_profile_link")
        if full_profile_link:
            print(f"\nExtracting co-authors for profile {index}/{len(unprocessed_profiles)}: {full_profile_link}")
            co_author_data = process_co_authors(full_profile_link, driver)
            if co_author_data:
                profile["co_author_details"] = co_author_data
                print(f"Co-author details extracted successfully.")
            else:
                print("No co-author data found.")

    save_to_json(profiles, input_file)

def main():
    input_file = "final_data1.json"

    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return

    driver = get_stealth_driver()

    print("Starting email and profile extraction process...")
    extract_emails_and_profiles(input_file, driver)

    print("\nStarting research interests extraction process...")
    extract_research_interests(input_file, driver)

    print("\nStarting co-author extraction process...")
    extract_co_authors(input_file, driver)

    driver.quit()
    print("\nProfile extraction process completed successfully.")

if __name__ == "__main__":
    main()
