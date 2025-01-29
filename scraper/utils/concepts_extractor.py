from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utils.common_utils import get_stealth_driver, random_delay

def fetch_and_parse_url(url, driver):
    """Fetch the webpage using Selenium and parse with BeautifulSoup."""
    print(f"Fetching research interests from: {url}")
    driver.get(url)
    random_delay()
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def extract_research_interests(soup):
    """Extract research interest concepts from the parsed HTML."""
    keyword_categories = soup.find("div", class_="keywordCategories")
    concepts = []

    if keyword_categories:
        for li in keyword_categories.find_all("li"):
            concept = li.get_text(strip=True)
            if concept:
                concepts.append(concept)

    return concepts if concepts else None

def format_research_url(full_profile_link):
    """Format the full profile link into the research interests page format."""
    base_url = "https://profiles.bu.edu/display/person/"
    person_name = full_profile_link.split("/")[-1].lower()
    research_url = f"{base_url}{person_name}/network/researchareas/categories"
    return research_url

def process_research_interests(full_profile_link, driver):
    """Fetch and extract research interests using Selenium."""
    research_url = format_research_url(full_profile_link)
    soup = fetch_and_parse_url(research_url, driver)
    if soup:
        return extract_research_interests(soup)
    return None
