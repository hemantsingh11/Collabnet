import json
from bs4 import BeautifulSoup

# Load the HTML file
html_file = "salma_abdalla_concepts.html"

with open(html_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

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

# Save extracted data to a JSON file
json_file = "research_interests.json"
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Data successfully saved to {json_file}")
