import requests
import json
from bs4 import BeautifulSoup

def fetch_and_parse_url(url):
    # Send an HTTP GET request
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
        return None

def extract_research_interests(soup):
    # Find the div containing research interests
    keyword_categories = soup.find("div", class_="keywordCategories")

    # Extract all concept names from <li> elements within the section
    concepts = []
    if keyword_categories:
        for li in keyword_categories.find_all("li"):
            concept = li.get_text(strip=True)
            if concept:
                concepts.append(concept)

    # Prepare the JSON structure
    data = {
        "research_interest": ", ".join(concepts)
    }

    return data

def save_to_json(data, filename="research_interests.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filename}")

# Main function
def main():
    url = "https://profiles.bu.edu/display/person/salma.abdalla/network/researchareas/categories"
    soup = fetch_and_parse_url(url)

    if soup:
        extracted_data = extract_research_interests(soup)
        save_to_json(extracted_data)

if __name__ == "__main__":
    main()
