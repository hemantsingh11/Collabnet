import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium_stealth import stealth

def scrape_name_link_pairs(output_json='BU_sph_directory_profiles_list.json'):
    # Configure Chrome options for headless + disable notifications
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")

    # Set up WebDriver via webdriver-manager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Enable stealth mode to reduce detection
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    
    # Target URL
    url = "https://www.bu.edu/sph/about/directory/"
    driver.get(url)
    
    # Wait briefly for JS content to load
    time.sleep(5)

    data = []
    seen = set()  # For deduplicating (name, link) pairs
    
    # Locate <li> elements that represent profiles
    li_xpath = '//ul[contains(@class, "profile-listing")]//li[contains(@class, "profile-item")]'
    profile_items = driver.find_elements(By.XPATH, li_xpath)
    
    for item in profile_items:
        try:
            # Extract the Full Name
            name_element = item.find_element(By.XPATH, './/span[contains(@class,"sph-profile-name-full")]')
            full_name = name_element.text.strip()

            # Extract the Profile Link
            link_element = item.find_element(By.XPATH, './/a[contains(@class,"sph-profile-basic-card")]')
            profile_link = link_element.get_attribute('href')

            # Extract the Position (if present)
            try:
                position_element = item.find_element(By.XPATH, './/h6[contains(@class,"sph-profile-main-position")]')
                position = position_element.text.strip()
            except:
                position = ""

            # Extract the Department (if present)
            try:
                dept_element = item.find_element(By.XPATH, './/div[contains(@class,"sph-profile-dept")]')
                department = dept_element.text.strip()
            except:
                department = ""

            # Deduplicate based on (name, link)
            key_tuple = (full_name, profile_link)
            if key_tuple not in seen:
                seen.add(key_tuple)
                
                data.append({
                    "name": full_name,
                    "profile_link": profile_link,
                    "position": position,
                    "department": department
                })
        
        except:
            # Skip if we can't find a name or link
            continue
    
    # Close the browser
    driver.quit()
    
    # Save data to JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    # Print total unique profiles found
    print(f"Total number of unique profile entries: {len(data)}")

if __name__ == "__main__":
    scrape_name_link_pairs()
