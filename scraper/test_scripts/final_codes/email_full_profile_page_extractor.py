import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    # Send an HTTP GET request
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
        return None

def extract_profile_info(soup):
    # Find email using the given XPath equivalent selector
    email_tag = soup.select_one('a.sph-profile-contact-link[href^="mailto:"]')
    email = email_tag['href'].replace('mailto:', '') if email_tag else None

    # Find full profile link using the given XPath equivalent selector
    profile_link_tag = soup.select_one('a.sph-profile-bumc-link')
    profile_link = profile_link_tag['href'] if profile_link_tag else None

    # Prepare JSON data
    data = {
        "email": email,
        "full_page_link": profile_link
    }

    return data

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filename}")

def main():
    url = "https://www.bu.edu/sph/profile/howard-cabral/"
    output_json = "email_full_profile_info.json"
    
    soup = fetch_html(url)

    if soup:
        extracted_data = extract_profile_info(soup)
        save_to_json(extracted_data, output_json)

if __name__ == "__main__":
    main()
