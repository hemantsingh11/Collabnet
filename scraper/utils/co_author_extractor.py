from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utils.common_utils import get_stealth_driver, random_delay

def fetch_and_parse_url(url, driver):
    """Use Selenium to fetch the webpage and parse it with BeautifulSoup."""
    print(f"Fetching co-author data from: {url}")
    driver.get(url)
    random_delay()  # Allow page to fully load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def extract_table_data(soup):
    """Extract co-author details from the parsed HTML."""
    all_titles = soup.find_all("b")
    tables = soup.find_all("div", class_="listTable")

    # Extract relevant titles
    relevant_titles = [b.get_text(strip=True) for b in all_titles if b.get_text(strip=True) in 
                       ["Co-Authors", "Co-Authors of Co-Authors", "Co-Author Connections"]]

    data = {}

    # Process each table and store data
    for title, table_div in zip(relevant_titles, tables):
        table = table_div.find("table")

        if not table:
            print(f"No table found under title: {title}")
            continue

        headers = [th.get_text(strip=True) for th in table.find("tr").find_all("th")]

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

def format_co_author_url(full_profile_link):
    """Format the full profile link into the co-author page format."""
    base_url = "https://profiles.bu.edu/display/person/"
    person_name = full_profile_link.split("/")[-1].lower()
    co_author_url = f"{base_url}{person_name}/network/coauthors/cluster"
    return co_author_url

def process_co_authors(full_profile_link, driver):
    """Fetch and extract co-author data using Selenium."""
    co_author_url = format_co_author_url(full_profile_link)
    soup = fetch_and_parse_url(co_author_url, driver)

    if soup:
        return extract_table_data(soup)
    return None
