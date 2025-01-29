import json
from bs4 import BeautifulSoup

def extract_profile_details(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Locate the panelMain section
    panel_main = soup.find('div', class_='panelMain')
    if not panel_main:
        print(json.dumps({"error": "Could not find panelMain section"}, indent=4))
        return

    # Locate the profile_websites section
    profile_websites_div = panel_main.find('div', id='profile_websites')
    if not profile_websites_div:
        print(json.dumps({"error": "Could not find profile_websites section"}, indent=4))
        return

    # Get the immediate previous sibling div
    parent_div = profile_websites_div.find_previous_sibling('div')
    if not parent_div:
        print(json.dumps({"error": "Could not find the div before profile_websites"}, indent=4))
        return

    # Extract text from the three nested divs inside parent_div
    nested_divs = parent_div.find_all('div', recursive=False)

    if len(nested_divs) < 3:
        print(json.dumps({"error": "Could not find three required divs inside the parent div"}, indent=4))
        return

    position = nested_divs[0].get_text(strip=True)
    school = nested_divs[1].get_text(strip=True)
    department = nested_divs[2].get_text(strip=True)

    # Construct the output JSON object
    profile_data = {
        "position": position,
        "school": school,
        "department": department
    }

    # Print the JSON output to console
    print(json.dumps(profile_data, indent=4))

# Run the function with the provided HTML file
if __name__ == "__main__":
    html_file = "Gregory_Cohen_profile_page.html"  # Replace with your file path
    extract_profile_details(html_file)
