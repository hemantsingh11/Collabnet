from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utils.common_utils import get_stealth_driver, random_delay

def fetch_and_parse_url(url, driver):
    """Fetch the webpage using Selenium and parse with BeautifulSoup."""
    print(f"Fetching page content from: {url}")
    driver.get(url)
    random_delay()
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def extract_email_and_profile_link(soup):
    """Extract email and full profile link from the given BeautifulSoup object."""
    print("Extracting profile information...")

    email_tag = soup.select_one('a.sph-profile-contact-link[href^="mailto:"]')
    email = email_tag['href'].replace('mailto:', '') if email_tag else None
    if email:
        print(f"Email found: {email}")
    else:
        print("No email found.")

    profile_link_tag = soup.select_one('a.sph-profile-bumc-link')
    profile_link = profile_link_tag['href'] if profile_link_tag else None
    if profile_link:
        print(f"Full profile link found: {profile_link}")
    else:
        print("No full profile link found.")

    return {
        "email": email,
        "full_profile_link": profile_link
    }

def process_profile(profile_url, driver):
    """Fetch and extract profile information using Selenium."""
    print(f"Processing profile: {profile_url}")
    soup = fetch_and_parse_url(profile_url, driver)
    if soup:
        return extract_email_and_profile_link(soup)
    print("Skipping profile due to fetch failure.")
    return None

def save_to_json(data, filename):
    """Save extracted data into a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filename}")
