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

# Max session duration in seconds (10 minutes = 600)
SESSION_DURATION = 600

def create_driver():
    """
    Creates and returns a new Selenium WebDriver for Chrome,
    preconfigured with stealth settings.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")

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
    2) For records whose 'position' contains 'professor', opens the profile_link.
    3) Extracts email (mailto) and full_profile_link (e.g., BUMC link).
    4) Updates those entries in-place in the SAME JSON.
    5) Prints a success message for each person's details fetched.
    6) Saves the JSON after *each* update (so data isn't lost if script is interrupted).
    7) Every 10 minutes, reinitialize (quit and recreate) the driver.
    """
    # Load the existing JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        all_profiles = json.load(f)

    # Create the driver for the first time
    driver = create_driver()
    session_start_time = time.time()

    updated_count = 0

    # Loop through each record in JSON
    for profile in all_profiles:
        position = profile.get("position", "")
        # Only proceed if "professor" is in the position (case-insensitive)
        if "professor" in position.lower():
            profile_link = profile.get("profile_link", "")
            if not profile_link:
                continue

            # Check if we've exceeded the 10-minute session duration
            elapsed = time.time() - session_start_time
            if elapsed > SESSION_DURATION:
                driver.quit()
                driver = create_driver()
                session_start_time = time.time()
                print("=== Session has been reset; new IP acquired. ===")

            # Navigate to the individual's page
            driver.get(profile_link)

            # Random delay to mimic human behavior
            time.sleep(random.uniform(2, 6))

            # Extract email
            email = ""
            wait = WebDriverWait(driver, 10)
            try:
                email_element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//a[@class="sph-profile-contact-link" and starts-with(@href,"mailto:")]')
                ))
                mailto_href = email_element.get_attribute("href")
                email = mailto_href.replace("mailto:", "").strip()
            except Exception as e:
                print(f"Email not found: {e}")
                email = ""

            # Extract full profile link
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

            # Update the JSON entry in-place
            profile["email"] = email
            profile["full_profile_link"] = full_profile_link

            updated_count += 1

            # Print success to console
            print(f"Successfully extracted info for {profile.get('name', 'N/A')}")
            print(f"  Email: {email}")
            print(f"  Full Profile: {full_profile_link}")

            # Save the JSON after each update
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(all_profiles, f, indent=4, ensure_ascii=False)

    driver.quit()

    # Print a final summary
    print(f"Updated {updated_count} entries with professor details.")
    print(f"Saved changes to {json_file} (after every update).")

if __name__ == "__main__":
    update_json_with_professor_details()
