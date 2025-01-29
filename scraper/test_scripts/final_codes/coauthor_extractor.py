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

def extract_table_data(soup):
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

    return data

def save_to_json(data, filename="co_authors_data.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {filename}")

# Main function
def main():
    url = "https://profiles.bu.edu/display/person/howard.cabral/network/coauthors/cluster"
    soup = fetch_and_parse_url(url)

    if soup:
        extracted_data = extract_table_data(soup)
        save_to_json(extracted_data)

if __name__ == "__main__":
    main()
