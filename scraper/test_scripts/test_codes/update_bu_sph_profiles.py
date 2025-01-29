import json
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#########################
# SMARTPROXY CREDENTIALS
#########################
SMARTPROXY_USERNAME = "spl3ormbj7"
SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"
SMARTPROXY_HOSTPORT = "us.smartproxy.com:10001"  # Using port 10001


# Max session duration in seconds (10 minutes = 600)
SESSION_DURATION = 600

def create_driver():
    """
    Creates and returns a new Selenium WebDriver for Chrome,
    preconfigured with Smartproxy + stealth settings.
    """
    proxy_string = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}"

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument(f"--proxy-server={proxy_string}")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Activate stealth mode
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    return driver

def update_json_with_professor_details(json_file='BU_sph_directory_profiles_list.json'):
    """
    1) Loads the existing JSON data (with 'name', 'profile_link', 'position', etc.).
    2) For records whose 'position' contains 'professor', opens the profile_link via Smartproxy.
    3) Extracts email (mailto) and full_profile_link (e.g., BUMC link).
    4) Updates those entries in-place in the SAME JSON.
    5) Prints a success message for each person's details fetched.
    6) Saves the JSON after *each* update (so data isn't lost if script is interrupted).
    7) Every 10 minutes, reinitialize (quit and recreate) the driver to get a fresh IP.
    """

    # 1. Load the existing JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        all_profiles = json.load(f)

    # Create the driver for the first time
    driver = create_driver()
    session_start_time = time.time()

    updated_count = 0

    # 2. Loop through each record in JSON
    for profile in all_profiles:
        position = profile.get("position", "")
        # Only proceed if "professor" is in the position (case-insensitive)
        if "professor" in position.lower():
            profile_link = profile.get("profile_link", "")
            if not profile_link:
                continue

            # (a) Check if we've exceeded the 10-minute session duration
            elapsed = time.time() - session_start_time
            if elapsed > SESSION_DURATION:
                # Close current driver and start a new one
                driver.quit()
                driver = create_driver()
                session_start_time = time.time()
                print("=== Session has been reset; new IP acquired. ===")

            # (b) Navigate to the individual's page
            driver.get(profile_link)

            # (c) Random delay to mimic human behavior
            time.sleep(random.uniform(2, 6))

            # (d) Extract email (if any)
            email = ""
            # (1) Extract email:
            # 1) Email extraction


            # Wait instance (up to 10 seconds for element to appear)
            wait = WebDriverWait(driver, 10)

            # 1) Extract email using explicit wait
            try:
                email_element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//a[@class="sph-profile-contact-link" and starts-with(@href,"mailto:")]')
                ))
                mailto_href = email_element.get_attribute("href")
                email = mailto_href.replace("mailto:", "").strip()
            except Exception as e:
                print(f"Email not found: {e}")
                email = ""

            # 2) Extract full profile link using explicit wait
            try:
                profile_bumc_element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//a[@class="sph-profile-bumc-link"]')
                ))
                full_profile_link = profile_bumc_element.get_attribute("href")
            except Exception as e:
                print(f"Full profile link not found: {e}")
                full_profile_link = ""

            print(f"Extracted Email: {email}")
            print(f"Extracted Full Profile Link: {full_profile_link}")




            # (f) Update the JSON entry in-place
            profile["email"] = email
            profile["full_profile_link"] = full_profile_link

            updated_count += 1

            # (g) Print success to console
            print(f"Successfully extracted info for {profile.get('name', 'N/A')}")
            print(f"  Email: {email}")
            print(f"  Full Profile: {full_profile_link}")

            # (h) Save the JSON after each update so data isn't lost
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(all_profiles, f, indent=4, ensure_ascii=False)

    # 3. Close the browser at the end
    driver.quit()

    # 4. Print a final summary
    print(f"Updated {updated_count} entries with professor details.")
    print(f"Saved changes to {json_file} (after every update).")

if __name__ == "__main__":
    update_json_with_professor_details()
