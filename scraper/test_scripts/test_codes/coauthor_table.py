import json
from bs4 import BeautifulSoup

# Load the saved HTML file
html_file = "salma_abdalla_profile.html"

with open(html_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find all section titles and corresponding tables
all_titles = soup.find_all("b")
tables = soup.find_all("div", class_="listTable")

# Filter titles to get only the relevant ones
relevant_titles = [b.get_text(strip=True) for b in all_titles if b.get_text(strip=True) in 
                   ["Co-Authors", "Co-Authors of Co-Authors", "Co-Author Connections"]]

# Dictionary to store extracted data
data = {}

# Process each table and store data
for title, table_div in zip(relevant_titles, tables):
    table = table_div.find("table")

    # Extract headers
    headers = [th.get_text(strip=True) for th in table.find("tr").find_all("th")]

    # Extract table rows
    table_data = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cells = row.find_all("td")
        row_data = {}
        for i, cell in enumerate(cells):
            link = cell.find("a")
            value = cell.get_text(strip=True).replace("\xa0", " ")  # Handle non-breaking spaces
            row_data[headers[i]] = {"value": value, "link": link["href"] if link else None}
        table_data.append(row_data)

    data[title] = table_data

# Save extracted data to JSON
json_file = "co_authors_data.json"
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Data successfully saved to {json_file}")
