import json
from selenium import webdriver
from bs4 import BeautifulSoup
from utils.common_utils import get_stealth_driver, random_delay

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"Updated JSON saved to {filename}")

def get_final_profile_link(initial_link, driver):
    try:
        driver.get(initial_link)
        random_delay()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        meta_redirect = soup.find('meta', attrs={"http-equiv": "refresh"})
        if meta_redirect:
            content = meta_redirect.get("content")
            if content and "url=" in content:
                return content.split("url=")[-1].strip()
        return driver.current_url
    except Exception as e:
        print(f"Request failed: {e}")
        return None

def fetch_html_content(profile_link, driver):
    try:
        driver.get(profile_link)
        random_delay()
        return driver.page_source
    except Exception as e:
        print(f"Request failed: {e}")
    return None

def extract_profile_details_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    panel_main = soup.find('div', class_='panelMain')
    if not panel_main:
        return None, None, None

    profile_websites_div = panel_main.find('div', id='profile_websites')
    if not profile_websites_div:
        return None, None, None

    parent_div = profile_websites_div.find_previous_sibling('div')
    if not parent_div:
        return None, None, None

    nested_divs = parent_div.find_all('div', recursive=False)
    if len(nested_divs) < 3:
        return None, None, None

    position = nested_divs[0].get_text(strip=True)
    school = nested_divs[1].get_text(strip=True)
    department = nested_divs[2].get_text(strip=True)

    return position, school, department

def update_json_with_profile(json_file, name, profile_link, driver):
    json_data = load_json(json_file)
    profile_entry = next((entry for entry in json_data if entry["name"] == name), None)

    if not profile_entry:
        print(f"{name} not found in JSON. Fetching profile...")

        final_profile_link = get_final_profile_link(profile_link, driver)
        if not final_profile_link:
            return json_data

        print(f"Final Profile Link: {final_profile_link}")
        html_content = fetch_html_content(final_profile_link, driver)
        if not html_content:
            return json_data

        position, school, department = extract_profile_details_from_html(html_content)
        if not (position and school and department):
            return json_data

        profile_entry = {
            "name": name,
            "profile_link": profile_link,
            "position": position,
            "department": department,
            "school": school,
            "email": "",
            "full_profile_link": final_profile_link,
            "co_author_details": {},
            "research_interest": []
        }
        json_data.append(profile_entry)

    return json_data
