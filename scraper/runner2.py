import json
import os
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from utils.coauthor_expansion import update_json_with_profile
from utils.concepts_extractor import process_research_interests
from utils.co_author_extractor import process_co_authors
from utils.common_utils import get_stealth_driver, random_delay


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

def get_stealth_driver():
    """Initialize a stealth Selenium driver in headless mode."""
    options = uc.ChromeOptions()
    options.headless = True  # Run in headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    ]
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(options=options)
    return driver

def random_delay():
    """Introduce random human-like delays to avoid detection."""
    delay = random.uniform(5, 15)
    jitter = random.uniform(0.5, 1.5)
    print(f"Sleeping for {delay + jitter:.2f} seconds...")
    time.sleep(delay + jitter)

def random_long_delay():
    """Introduce a random delay of 1 to 2 minutes after every 5 to 10 minutes."""
    long_delay = random.randint(300, 600)  # 5 to 10 minutes in seconds
    short_delay = random.randint(60, 120)  # 1 to 2 minutes in seconds
    print(f"Waiting for {short_delay // 60} minute(s)...")
    time.sleep(short_delay)
    return long_delay

def process_profile(json_file, profile, driver):
    """Extract and update research interests and co-author details using Selenium."""
    print(f"Processing profile for: {profile['name']}")
    random_delay()
    
    research_interests = process_research_interests(profile["full_profile_link"], driver)
    if research_interests:
        profile["research_interest"] = research_interests
        print(f"Research interests found for {profile['name']}: {len(research_interests)} interests.")

    co_author_details = process_co_authors(profile["full_profile_link"], driver)
    if co_author_details:
        profile["co_author_details"] = co_author_details
        print(f"Co-author details extracted successfully for {profile['name']}.")

def process_co_authors_of_selected_profile(json_file, selected_name, co_author_limit):
    """Process only the co-authors of the given profile and extract their details sequentially, skipping already processed profiles."""
    data = load_json(json_file)
    driver = get_stealth_driver()

    try:
        profile = next((p for p in data if p["name"] == selected_name), None)
        if not profile:
            print(f"Profile for {selected_name} not found.")
            return

        print(f"Fetching co-authors of: {selected_name}")
        co_authors = profile.get("co_author_details", {}).get("Co-Authors", [])[:co_author_limit]

        for author in co_authors:
            name = format_name(author["Name"]["value"])
            profile_link = author["Name"]["link"]

            existing_profile = next((p for p in data if p["name"] == name), None)
            if existing_profile and existing_profile.get("research_interest") and existing_profile.get("co_author_details"):
                print(f"Skipping already processed co-author: {name}")
                continue

            print(f"\n--- Processing co-author: {name} ---")
            random_delay()

            updated_data = update_json_with_profile(json_file, name, profile_link, driver)

            if updated_data:
                save_json(json_file, updated_data)
                print(f"{name} profile saved successfully.")
                data = load_json(json_file)

            new_profile = next((p for p in data if p["name"] == name), None)
            if new_profile:
                print(f"Processing research interests and co-authors for: {name}")
                random_delay()
                research_interests = process_research_interests(new_profile["full_profile_link"], driver)
                if research_interests:
                    new_profile["research_interest"] = research_interests
                    print(f"Research interests found for {name}: {len(research_interests)}")

                co_author_details = process_co_authors(new_profile["full_profile_link"], driver)
                if co_author_details:
                    new_profile["co_author_details"] = co_author_details
                    print(f"Co-author details extracted successfully for {name}.")

                save_json(json_file, data)
                print(f"{name}'s profile fully updated in JSON.")
    finally:
        try:
            if driver:
                driver.quit()
                print("WebDriver closed successfully.")
        except OSError:
            print("WebDriver already closed or handle invalid.")



# if __name__ == "__main__":
#     selected_name = "Laura White"
#     co_author_limit = 5
#     process_co_authors_of_selected_profile("final_data1.json", selected_name, co_author_limit)
# if __name__ == "__main__":
    
    
if __name__ == "__main__":
    process_count = 0

    names = [
    "Marilyn Moy",
    "John Ney",
    "Emily Wan",
    "Denise Wong",
    "Guneet Jasuja",
    "Jay Orlander",
    "Seppo Rinne",
    "Bahaa Abdellatif",
    "Julia Prentice",
    "Hillary Mull",
    "Sivagaminathan Palani",
    "Paul Conlin",
    "Samantha Auty",
    "Lily Yan",
    "Megan Cole Brahim",
    "Nicole Huberfeld ",
    "Anna Goldman",
    "Paul Shafer",
    "Allegra Gordon",
    "Lynsie Ranker",
    "Michael Stein"
]


    
    co_author_limit = 5
    json_file = "final_data1.json"

    for name in names:
        print(f"\nStarting processing for: {name}")
        process_co_authors_of_selected_profile(json_file, name, co_author_limit)
        print(f"Completed processing for: {name}")
        
        process_count += 1
        if process_count % random.randint(5, 10) == 0:
            wait_time = random_long_delay()
            print(f"Resuming processing after {wait_time // 60} minute(s)...")

    print("\nAll profiles processed successfully.")
