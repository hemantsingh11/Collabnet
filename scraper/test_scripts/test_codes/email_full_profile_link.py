import json
from bs4 import BeautifulSoup

def extract_profile_info(html_file, output_json):
    # Load the saved HTML file
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

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

    # Save extracted data to a JSON file
    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Data successfully saved to {output_json}")

# Example usage
if __name__ == "__main__":
    html_file = "salma_abdalla_profile_page.html"  # Change to the actual file path
    output_json = "profile_info.json"
    extract_profile_info(html_file, output_json)
