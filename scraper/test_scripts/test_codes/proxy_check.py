# # # # # # # # # # import requests

# # # # # # # # # # SMARTPROXY_USERNAME = "spl3ormbj7"
# # # # # # # # # # SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"
# # # # # # # # # # SMARTPROXY_HOSTPORT = "us.smartproxy.com:10001"

# # # # # # # # # # proxy = {
# # # # # # # # # #     "http": f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}",
# # # # # # # # # #     "https": f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}",
# # # # # # # # # # }

# # # # # # # # # # try:
# # # # # # # # # #     response = requests.get("http://ipinfo.io/json", proxies=proxy, timeout=10)
# # # # # # # # # #     print(response.json())  # Check if the IP belongs to the USA
# # # # # # # # # # except requests.exceptions.RequestException as e:
# # # # # # # # # #     print(f"Proxy connection failed: {e}")




# # # # # # # # # import time
# # # # # # # # # from selenium import webdriver
# # # # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # # # # # from selenium.webdriver.common.by import By
# # # # # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # # # # # Smartproxy credentials
# # # # # # # # # SMARTPROXY_USERNAME = "spl3ormbj7"
# # # # # # # # # SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"
# # # # # # # # # SMARTPROXY_HOSTPORT = "us.smartproxy.com:10001"  # Use US-based proxy

# # # # # # # # # # Construct proxy string
# # # # # # # # # proxy_string = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}"

# # # # # # # # # # Set up Chrome options
# # # # # # # # # chrome_options = Options()
# # # # # # # # # chrome_options.add_argument(f"--proxy-server={proxy_string}")
# # # # # # # # # chrome_options.add_argument("--headless")  # Run headless for testing (set to False for debugging)
# # # # # # # # # chrome_options.add_argument("--disable-gpu")
# # # # # # # # # chrome_options.add_argument("--no-sandbox")
# # # # # # # # # chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # # # # # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # # # # # chrome_options.add_argument("--disable-infobars")
# # # # # # # # # chrome_options.add_argument("--ignore-certificate-errors")
# # # # # # # # # chrome_options.add_argument("--log-level=3")  # Suppress unnecessary logs

# # # # # # # # # # Create WebDriver
# # # # # # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # # # # # # Function to test website access
# # # # # # # # # def test_website_access():
# # # # # # # # #     try:
# # # # # # # # #         print("Testing website access...")

# # # # # # # # #         # Set page load timeout (increase if proxy is slow)
# # # # # # # # #         driver.set_page_load_timeout(60)

# # # # # # # # #         # Navigate to the test URL
# # # # # # # # #         driver.get("https://www.bu.edu/sph/profile/salma-abdalla/")
# # # # # # # # #         time.sleep(5)  # Allow time for page to load

# # # # # # # # #         # Check if a key element (e.g., profile name) exists
# # # # # # # # #         try:
# # # # # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # # # # #             )
# # # # # # # # #             print("Success: Website loaded successfully!")
# # # # # # # # #             print("Profile Name Found:", element.text)
# # # # # # # # #         except:
# # # # # # # # #             print("Failure: Profile page did not load correctly.")

# # # # # # # # #         # Save a screenshot for verification
# # # # # # # # #         driver.save_screenshot("website_test_screenshot.png")
# # # # # # # # #         print("Screenshot saved as 'website_test_screenshot.png'")

# # # # # # # # #     except Exception as e:
# # # # # # # # #         print(f"Failed to access the website: {e}")

# # # # # # # # #     finally:
# # # # # # # # #         driver.quit()

# # # # # # # # # # Run the test
# # # # # # # # # test_website_access()



# # # # # # # # import requests
# # # # # # # # import time
# # # # # # # # from selenium import webdriver
# # # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # # # # from selenium.webdriver.common.by import By
# # # # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # # # # Smartproxy credentials
# # # # # # # # SMARTPROXY_USERNAME = "spl3ormbj7"
# # # # # # # # SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"
# # # # # # # # SMARTPROXY_HOSTPORT = "us.smartproxy.com:10001"

# # # # # # # # # Construct proxy strings
# # # # # # # # http_proxy = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}"
# # # # # # # # socks5_proxy = f"socks5://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}"

# # # # # # # # # Test URL (target website)
# # # # # # # # TEST_URL = "https://www.bu.edu/sph/profile/salma-abdalla/"

# # # # # # # # # Function to test proxy connectivity with requests
# # # # # # # # def test_proxy_with_requests(proxy_url):
# # # # # # # #     print("\n[1] Testing proxy connection via requests module...")
# # # # # # # #     proxy = {
# # # # # # # #         "http": proxy_url,
# # # # # # # #         "https": proxy_url,
# # # # # # # #     }
# # # # # # # #     try:
# # # # # # # #         response = requests.get("http://ipinfo.io/json", proxies=proxy, timeout=10)
# # # # # # # #         print("Proxy works! Your IP info:", response.json())
# # # # # # # #     except requests.exceptions.RequestException as e:
# # # # # # # #         print(f"Proxy failed: {e}")

# # # # # # # # # Function to test website access via Selenium
# # # # # # # # def test_website_with_selenium(proxy_type="http", headless=True):
# # # # # # # #     print(f"\n[2] Testing website access via Selenium with {proxy_type} proxy, headless={headless}...")

# # # # # # # #     # Choose proxy type
# # # # # # # #     proxy_url = http_proxy if proxy_type == "http" else socks5_proxy

# # # # # # # #     chrome_options = Options()
# # # # # # # #     chrome_options.add_argument(f"--proxy-server={proxy_url}")
    
# # # # # # # #     if headless:
# # # # # # # #         chrome_options.add_argument("--headless")  # Run headless
# # # # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # # # #     chrome_options.add_argument("--no-sandbox")
# # # # # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # # # #     chrome_options.add_argument("--disable-infobars")
# # # # # # # #     chrome_options.add_argument("--ignore-certificate-errors")

# # # # # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # # # #     # Set timeout
# # # # # # # #     driver.set_page_load_timeout(60)

# # # # # # # #     try:
# # # # # # # #         driver.get(TEST_URL)
# # # # # # # #         time.sleep(5)

# # # # # # # #         # Check if the page loaded properly
# # # # # # # #         try:
# # # # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # # # #             )
# # # # # # # #             print("Success: Website loaded successfully!")
# # # # # # # #             print("Profile Name Found:", element.text)
# # # # # # # #         except:
# # # # # # # #             print("Failure: Profile page did not load correctly.")

# # # # # # # #         # Save screenshot and page source for further analysis
# # # # # # # #         driver.save_screenshot("website_test_screenshot.png")
# # # # # # # #         with open("website_test_source.html", "w", encoding="utf-8") as f:
# # # # # # # #             f.write(driver.page_source)
# # # # # # # #         print("Screenshot and page source saved.")
# # # # # # # #     except Exception as e:
# # # # # # # #         print(f"Failed to access the website: {e}")
# # # # # # # #     finally:
# # # # # # # #         driver.quit()

# # # # # # # # # Function to test website without proxy
# # # # # # # # def test_without_proxy(headless=True):
# # # # # # # #     print(f"\n[3] Testing website access without proxy, headless={headless}...")

# # # # # # # #     chrome_options = Options()
# # # # # # # #     if headless:
# # # # # # # #         chrome_options.add_argument("--headless")  # Run headless
# # # # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # # # #     chrome_options.add_argument("--no-sandbox")
# # # # # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # # # #     chrome_options.add_argument("--disable-infobars")

# # # # # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # # # #     # Set timeout
# # # # # # # #     driver.set_page_load_timeout(60)

# # # # # # # #     try:
# # # # # # # #         driver.get(TEST_URL)
# # # # # # # #         time.sleep(5)

# # # # # # # #         # Check if the page loaded properly
# # # # # # # #         try:
# # # # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # # # #             )
# # # # # # # #             print("Success: Website loaded successfully without proxy!")
# # # # # # # #             print("Profile Name Found:", element.text)
# # # # # # # #         except:
# # # # # # # #             print("Failure: Profile page did not load correctly without proxy.")

# # # # # # # #         # Save screenshot and page source for further analysis
# # # # # # # #         driver.save_screenshot("website_no_proxy_screenshot.png")
# # # # # # # #         with open("website_no_proxy_source.html", "w", encoding="utf-8") as f:
# # # # # # # #             f.write(driver.page_source)
# # # # # # # #         print("Screenshot and page source saved (no proxy).")
# # # # # # # #     except Exception as e:
# # # # # # # #         print(f"Failed to access the website without proxy: {e}")
# # # # # # # #     finally:
# # # # # # # #         driver.quit()


# # # # # # # # # Run tests
# # # # # # # # if __name__ == "__main__":
# # # # # # # #     # 1. Test proxy with requests
# # # # # # # #     test_proxy_with_requests(http_proxy)
    
# # # # # # # #     # 2. Test with Selenium using HTTP proxy (headless and non-headless)
# # # # # # # #     test_website_with_selenium(proxy_type="http", headless=True)  # Headless mode
# # # # # # # #     test_website_with_selenium(proxy_type="http", headless=False)  # Visible mode
    
# # # # # # # #     # 3. Test with Selenium using SOCKS5 proxy (headless and non-headless)
# # # # # # # #     test_website_with_selenium(proxy_type="socks5", headless=True)  # Headless mode
# # # # # # # #     test_website_with_selenium(proxy_type="socks5", headless=False)  # Visible mode

# # # # # # # #     # 4. Test website without proxy
# # # # # # # #     test_without_proxy(headless=True)  # Headless mode
# # # # # # # #     test_without_proxy(headless=False)  # Visible mode




# # # # # # # import requests
# # # # # # # import time
# # # # # # # import random
# # # # # # # from selenium import webdriver
# # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # # # from selenium.webdriver.common.by import By
# # # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # # # Smartproxy credentials
# # # # # # # SMARTPROXY_USERNAME = "spl3ormbj7"
# # # # # # # SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"
# # # # # # # SMARTPROXY_HOSTPORT = "gate.smartproxy.com:10001"  # Rotating residential proxy

# # # # # # # # Target URL to test
# # # # # # # TEST_URL = "https://www.bu.edu/sph/profile/salma-abdalla/"

# # # # # # # # Proxy setup for requests
# # # # # # # proxy = {
# # # # # # #     "http": f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}",
# # # # # # #     "https": f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HOSTPORT}",
# # # # # # # }

# # # # # # # def test_proxy_with_requests():
# # # # # # #     """
# # # # # # #     Test the Smartproxy rotating proxy with requests to confirm it's working and rotating IPs.
# # # # # # #     """
# # # # # # #     print("\n[1] Testing proxy connection via requests module...")

# # # # # # #     try:
# # # # # # #         response = requests.get("http://ipinfo.io/json", proxies=proxy, timeout=10)
# # # # # # #         ip_info = response.json()
# # # # # # #         print("Proxy is working. Your IP info:", ip_info)
# # # # # # #         return ip_info['ip']
# # # # # # #     except requests.exceptions.RequestException as e:
# # # # # # #         print(f"Proxy failed: {e}")
# # # # # # #         return None

# # # # # # # def test_website_with_selenium(headless=True):
# # # # # # #     """
# # # # # # #     Test the website using Selenium to check if the proxy allows loading the profile page.
# # # # # # #     """
# # # # # # #     print(f"\n[2] Testing website access via Selenium (headless={headless})...")

# # # # # # #     chrome_options = Options()
# # # # # # #     chrome_options.add_argument(f"--proxy-server={proxy['http']}")

# # # # # # #     if headless:
# # # # # # #         chrome_options.add_argument("--headless")  # Run headless
# # # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # # #     chrome_options.add_argument("--no-sandbox")
# # # # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # # #     chrome_options.add_argument("--disable-infobars")
# # # # # # #     chrome_options.add_argument("--ignore-certificate-errors")
# # # # # # #     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# # # # # # #     chrome_options.add_argument("window-size=1280x1024")

# # # # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # # #     try:
# # # # # # #         driver.set_page_load_timeout(60)
# # # # # # #         driver.get(TEST_URL)
# # # # # # #         time.sleep(random.uniform(5, 10))  # Random sleep to mimic human behavior

# # # # # # #         # Check if the page loaded properly
# # # # # # #         try:
# # # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # # #             )
# # # # # # #             print("Success: Website loaded successfully!")
# # # # # # #             print("Profile Name Found:", element.text)
# # # # # # #         except:
# # # # # # #             print("Failure: Profile page did not load correctly.")

# # # # # # #         # Save screenshot and page source for debugging
# # # # # # #         driver.save_screenshot("selenium_test_screenshot.png")
# # # # # # #         with open("selenium_test_source.html", "w", encoding="utf-8") as f:
# # # # # # #             f.write(driver.page_source)
# # # # # # #         print("Screenshot and page source saved.")
    
# # # # # # #     except Exception as e:
# # # # # # #         print(f"Failed to access the website: {e}")
    
# # # # # # #     finally:
# # # # # # #         driver.quit()

# # # # # # # def test_without_proxy(headless=True):
# # # # # # #     """
# # # # # # #     Test the website without using proxy to confirm the website loads normally.
# # # # # # #     """
# # # # # # #     print(f"\n[3] Testing website access without proxy (headless={headless})...")

# # # # # # #     chrome_options = Options()
# # # # # # #     if headless:
# # # # # # #         chrome_options.add_argument("--headless")  # Run headless
# # # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # # #     chrome_options.add_argument("--no-sandbox")
# # # # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # # #     chrome_options.add_argument("--disable-infobars")

# # # # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # # #     try:
# # # # # # #         driver.set_page_load_timeout(60)
# # # # # # #         driver.get(TEST_URL)
# # # # # # #         time.sleep(random.uniform(5, 10))  # Random sleep

# # # # # # #         # Check if the page loaded properly
# # # # # # #         try:
# # # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # # #             )
# # # # # # #             print("Success: Website loaded successfully without proxy!")
# # # # # # #             print("Profile Name Found:", element.text)
# # # # # # #         except:
# # # # # # #             print("Failure: Profile page did not load correctly without proxy.")

# # # # # # #         # Save screenshot and page source for further analysis
# # # # # # #         driver.save_screenshot("no_proxy_screenshot.png")
# # # # # # #         with open("no_proxy_source.html", "w", encoding="utf-8") as f:
# # # # # # #             f.write(driver.page_source)
# # # # # # #         print("Screenshot and page source saved (no proxy).")
    
# # # # # # #     except Exception as e:
# # # # # # #         print(f"Failed to access the website without proxy: {e}")

# # # # # # #     finally:
# # # # # # #         driver.quit()

# # # # # # # if __name__ == "__main__":
# # # # # # #     # 1. Test the proxy with requests to confirm rotation
# # # # # # #     ip1 = test_proxy_with_requests()
# # # # # # #     time.sleep(5)  # Wait before second test
# # # # # # #     ip2 = test_proxy_with_requests()

# # # # # # #     if ip1 and ip2 and ip1 != ip2:
# # # # # # #         print("\nProxy IPs are rotating successfully!")
# # # # # # #     else:
# # # # # # #         print("\nProxy IPs are NOT rotating.")

# # # # # # #     # 2. Test website access with Selenium (headless and non-headless)
# # # # # # #     test_website_with_selenium(headless=True)  # Headless mode
# # # # # # #     test_website_with_selenium(headless=False)  # Visible mode

# # # # # # #     # 3. Test website access without proxy
# # # # # # #     test_without_proxy(headless=True)  # Headless mode
# # # # # # #     test_without_proxy(headless=False)  # Visible mode



# # # # # # import requests
# # # # # # import time
# # # # # # import random
# # # # # # from selenium import webdriver
# # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # # from selenium.webdriver.common.by import By
# # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # # Smartproxy credentials
# # # # # # SMARTPROXY_USERNAME = "spl3ormbj7"
# # # # # # SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"
# # # # # # SMARTPROXY_HTTP_HOSTPORT = "us.smartproxy.com:10001"  # Ensure US IPs
# # # # # # SMARTPROXY_SOCKS5_HOSTPORT = "us.smartproxy.com:10001"  # SOCKS5 for better masking

# # # # # # # Target URL to test
# # # # # # TEST_URL = "https://www.bu.edu/sph/profile/salma-abdalla/"

# # # # # # # Proxy configuration
# # # # # # http_proxy = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HTTP_HOSTPORT}"
# # # # # # socks5_proxy = f"socks5://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_SOCKS5_HOSTPORT}"

# # # # # # # Function to check the current IP of the proxy
# # # # # # def check_proxy(proxy_type="http"):
# # # # # #     print(f"\n[1] Checking {proxy_type.upper()} proxy IP...")
# # # # # #     proxy = {
# # # # # #         "http": http_proxy if proxy_type == "http" else socks5_proxy,
# # # # # #         "https": http_proxy if proxy_type == "http" else socks5_proxy,
# # # # # #     }

# # # # # #     try:
# # # # # #         response = requests.get("http://ipinfo.io/json", proxies=proxy, timeout=10)
# # # # # #         ip_info = response.json()
# # # # # #         print("Proxy is working. Your IP info:", ip_info)
# # # # # #         if ip_info.get('country') != "US":
# # # # # #             print("Warning: Proxy is NOT from the US!")
# # # # # #         else:
# # # # # #             print("Success: Proxy is from the US.")
# # # # # #     except requests.exceptions.RequestException as e:
# # # # # #         print(f"Proxy failed: {e}")

# # # # # # # Function to test website access via Selenium
# # # # # # def test_website_with_selenium(proxy_type="http", headless=True):
# # # # # #     print(f"\n[2] Testing website access via Selenium using {proxy_type.upper()} proxy (headless={headless})...")

# # # # # #     proxy_url = http_proxy if proxy_type == "http" else socks5_proxy

# # # # # #     chrome_options = Options()
# # # # # #     chrome_options.add_argument(f"--proxy-server={proxy_url}")
# # # # # #     if headless:
# # # # # #         chrome_options.add_argument("--headless")
# # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # #     chrome_options.add_argument("--no-sandbox")
# # # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # #     chrome_options.add_argument("--disable-infobars")
# # # # # #     chrome_options.add_argument("--ignore-certificate-errors")
# # # # # #     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# # # # # #     chrome_options.add_argument("window-size=1280x1024")

# # # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # #     try:
# # # # # #         driver.set_page_load_timeout(60)
# # # # # #         driver.get(TEST_URL)
# # # # # #         time.sleep(random.uniform(5, 10))  # Random sleep to mimic human behavior

# # # # # #         # Check if the page loaded properly
# # # # # #         try:
# # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # #             )
# # # # # #             print("Success: Website loaded successfully!")
# # # # # #             print("Profile Name Found:", element.text)
# # # # # #         except:
# # # # # #             print("Failure: Profile page did not load correctly.")

# # # # # #         # Save screenshot and page source for debugging
# # # # # #         driver.save_screenshot(f"selenium_{proxy_type}_screenshot.png")
# # # # # #         with open(f"selenium_{proxy_type}_source.html", "w", encoding="utf-8") as f:
# # # # # #             f.write(driver.page_source)
# # # # # #         print(f"Screenshot and page source saved for {proxy_type}.")
    
# # # # # #     except Exception as e:
# # # # # #         print(f"Failed to access the website: {e}")
    
# # # # # #     finally:
# # # # # #         driver.quit()

# # # # # # # Function to test website without using a proxy
# # # # # # def test_without_proxy(headless=True):
# # # # # #     print(f"\n[3] Testing website access without proxy (headless={headless})...")

# # # # # #     chrome_options = Options()
# # # # # #     if headless:
# # # # # #         chrome_options.add_argument("--headless")
# # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # #     chrome_options.add_argument("--no-sandbox")
# # # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # #     chrome_options.add_argument("--disable-infobars")

# # # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # # #     try:
# # # # # #         driver.set_page_load_timeout(60)
# # # # # #         driver.get(TEST_URL)
# # # # # #         time.sleep(random.uniform(5, 10))  # Random sleep

# # # # # #         # Check if the page loaded properly
# # # # # #         try:
# # # # # #             element = WebDriverWait(driver, 10).until(
# # # # # #                 EC.presence_of_element_located((By.TAG_NAME, "h1"))
# # # # # #             )
# # # # # #             print("Success: Website loaded successfully without proxy!")
# # # # # #             print("Profile Name Found:", element.text)
# # # # # #         except:
# # # # # #             print("Failure: Profile page did not load correctly without proxy.")

# # # # # #         # Save screenshot and page source for further analysis
# # # # # #         driver.save_screenshot("no_proxy_screenshot.png")
# # # # # #         with open("no_proxy_source.html", "w", encoding="utf-8") as f:
# # # # # #             f.write(driver.page_source)
# # # # # #         print("Screenshot and page source saved (no proxy).")
    
# # # # # #     except Exception as e:
# # # # # #         print(f"Failed to access the website without proxy: {e}")

# # # # # #     finally:
# # # # # #         driver.quit()

# # # # # # if __name__ == "__main__":
# # # # # #     # 1. Test proxy IPs to ensure they are from the US
# # # # # #     check_proxy(proxy_type="http")
# # # # # #     time.sleep(5)
# # # # # #     check_proxy(proxy_type="socks5")

# # # # # #     # 2. Test website access with Selenium using HTTP proxy
# # # # # #     test_website_with_selenium(proxy_type="http", headless=True)
# # # # # #     test_website_with_selenium(proxy_type="http", headless=False)

# # # # # #     # 3. Test website access with Selenium using SOCKS5 proxy
# # # # # #     test_website_with_selenium(proxy_type="socks5", headless=True)
# # # # # #     test_website_with_selenium(proxy_type="socks5", headless=False)

# # # # # #     # 4. Test website access without proxy
# # # # # #     test_without_proxy(headless=True)
# # # # # #     test_without_proxy(headless=False)






# # # # # import requests
# # # # # import random
# # # # # import time
# # # # # from fake_useragent import UserAgent
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.chrome.options import Options
# # # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # # # Smartproxy credentials
# # # # # SMARTPROXY_USERNAME = "spl3ormbj7"
# # # # # SMARTPROXY_PASSWORD = "7zQsTd+r89cwarPa4M"

# # # # # # Use rotating proxies from Smartproxy
# # # # # SMARTPROXY_HTTP_HOSTPORT = "us.smartproxy.com:10001"  # HTTP rotating proxy
# # # # # SMARTPROXY_SOCKS5_HOSTPORT = "us.smartproxy.com:10001"  # SOCKS5 rotating proxy

# # # # # # Profile page to scrape
# # # # # PROFILE_URL = "https://www.bu.edu/sph/profile/salma-abdalla/"

# # # # # # Generate random User-Agent
# # # # # ua = UserAgent()
# # # # # USER_AGENT = ua.random

# # # # # # Proxy format
# # # # # http_proxy = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_HTTP_HOSTPORT}"
# # # # # socks5_proxy = f"socks5://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@{SMARTPROXY_SOCKS5_HOSTPORT}"

# # # # # # Choose proxy type (http or socks5)
# # # # # PROXY_TYPE = "http"  # Change to "socks5" if needed

# # # # # if PROXY_TYPE == "http":
# # # # #     proxy_address = http_proxy
# # # # # else:
# # # # #     proxy_address = socks5_proxy

# # # # # # Random sleep function to mimic human behavior
# # # # # def random_wait():
# # # # #     wait_time = random.uniform(30, 60)
# # # # #     print(f"Sleeping for {wait_time:.2f} seconds to mimic human behavior...")
# # # # #     time.sleep(wait_time)

# # # # # # Function to scrape using requests
# # # # # def scrape_with_requests():
# # # # #     print("\n[1] Scraping using requests with Smartproxy...")

# # # # #     headers = {
# # # # #         "User-Agent": USER_AGENT,
# # # # #         "Accept-Language": "en-US,en;q=0.9",
# # # # #     }

# # # # #     proxies = {
# # # # #         "http": proxy_address,
# # # # #         "https": proxy_address,
# # # # #     }

# # # # #     try:
# # # # #         response = requests.get(PROFILE_URL, headers=headers, proxies=proxies, timeout=20)
# # # # #         if response.status_code == 200:
# # # # #             print("Success! Profile page loaded.")
# # # # #             print(response.text[:500])  # Print snippet of content
# # # # #         else:
# # # # #             print(f"Failed to fetch profile page. Status code: {response.status_code}")
# # # # #     except requests.exceptions.RequestException as e:
# # # # #         print(f"Error during request: {e}")

# # # # # # Function to scrape using Selenium
# # # # # def scrape_with_selenium(headless=True):
# # # # #     print(f"\n[2] Scraping using Selenium with Smartproxy (headless={headless})...")

# # # # #     chrome_options = Options()
# # # # #     chrome_options.add_argument(f"--proxy-server={proxy_address}")
# # # # #     chrome_options.add_argument(f"user-agent={USER_AGENT}")

# # # # #     if headless:
# # # # #         chrome_options.add_argument("--headless")  # Run headless for better stealth

# # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# # # # #     chrome_options.add_argument("--no-sandbox")
# # # # #     chrome_options.add_argument("--disable-gpu")
# # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # #     chrome_options.add_argument("--ignore-certificate-errors")
# # # # #     chrome_options.add_argument("window-size=1280x1024")

# # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # #     try:
# # # # #         driver.set_page_load_timeout(60)
# # # # #         driver.get(PROFILE_URL)
# # # # #         random_wait()

# # # # #         # Extract the profile name (h1 tag)
# # # # #         try:
# # # # #             profile_name = driver.find_element("tag name", "h1").text
# # # # #             print("Profile Name Found:", profile_name)
# # # # #         except:
# # # # #             print("Failed to find profile name.")

# # # # #         # Save page source and screenshot for debugging
# # # # #         driver.save_screenshot(f"selenium_{PROXY_TYPE}_screenshot.png")
# # # # #         with open(f"selenium_{PROXY_TYPE}_source.html", "w", encoding="utf-8") as f:
# # # # #             f.write(driver.page_source)
# # # # #         print(f"Screenshot and page source saved for {PROXY_TYPE}.")

# # # # #     except Exception as e:
# # # # #         print(f"Error while loading page: {e}")
    
# # # # #     finally:
# # # # #         driver.quit()

# # # # # # Function to scrape without proxy
# # # # # def scrape_without_proxy():
# # # # #     print("\n[3] Scraping without proxy for comparison...")

# # # # #     chrome_options = Options()
# # # # #     chrome_options.add_argument(f"user-agent={USER_AGENT}")
# # # # #     chrome_options.add_argument("--headless")

# # # # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # # # #     try:
# # # # #         driver.get(PROFILE_URL)
# # # # #         random_wait()

# # # # #         profile_name = driver.find_element("tag name", "h1").text
# # # # #         print("Profile Name (without proxy):", profile_name)

# # # # #         driver.save_screenshot("no_proxy_screenshot.png")
# # # # #         print("Screenshot saved without proxy.")

# # # # #     except Exception as e:
# # # # #         print(f"Failed to load page without proxy: {e}")

# # # # #     finally:
# # # # #         driver.quit()

# # # # # # Run the scraping tests
# # # # # if __name__ == "__main__":
# # # # #     # Test scraping with requests
# # # # #     scrape_with_requests()

# # # # #     # Test scraping with Selenium (headless and non-headless)
# # # # #     scrape_with_selenium(headless=True)
# # # # #     scrape_with_selenium(headless=False)

# # # # #     # Test scraping without proxy for comparison
# # # # #     scrape_without_proxy()





# # # # #!/usr/bin/env python

# # # # print('If you get error "ImportError: No module named \'six\'" install six:\n' +
# # # #       '$ pip install six')
# # # # print('To enable your free eval account and get CUSTOMER, YOURZONE, and ' +
# # # #       'YOURPASS, please contact sales@brightdata.com')

# # # # import sys

# # # # # Proxy credentials (Update these with your own credentials)
# # # # PROXY_URL = 'http://brd-customer-hl_b81fbb29-zone-residential_proxy2-country-us:mpq3drhs0ama@brd.superproxy.io:33335'

# # # # TARGET_URL = 'https://geo.brdtest.com/mygeo.json'  # BrightData test page to verify proxy IP

# # # # # Python 2 compatibility
# # # # if sys.version_info[0] == 2:
# # # #     import six
# # # #     from six.moves.urllib import request

# # # #     opener = request.build_opener(
# # # #         request.ProxyHandler(
# # # #             {'http': PROXY_URL, 'https': PROXY_URL}
# # # #         )
# # # #     )
# # # #     print("Using proxy to access:", TARGET_URL)
# # # #     response = opener.open(TARGET_URL).read()
# # # #     print("Proxy response:", response)

# # # # # Python 3 code
# # # # elif sys.version_info[0] == 3:
# # # #     import urllib.request

# # # #     proxy_handler = urllib.request.ProxyHandler({
# # # #         'http': PROXY_URL,
# # # #         'https': PROXY_URL
# # # #     })
    
# # # #     opener = urllib.request.build_opener(proxy_handler)

# # # #     try:
# # # #         print("Using proxy to access:", TARGET_URL)
# # # #         response = opener.open(TARGET_URL)
# # # #         print("Proxy response:", response.read().decode())
# # # #     except Exception as e:
# # # #         print("Error accessing via proxy:", e)





# # # import ssl
# # # import urllib.request

# # # PROXY_URL = 'http://brd-customer-hl_b81fbb29-zone-residential_proxy2-country-us:mpq3drhs0ama@brd.superproxy.io:33335'
# # # TARGET_URL = 'https://geo.brdtest.com/mygeo.json'

# # # # Create an unverified SSL context
# # # context = ssl._create_unverified_context()

# # # proxy_handler = urllib.request.ProxyHandler({
# # #     'http': PROXY_URL,
# # #     'https': PROXY_URL
# # # })

# # # opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=context))

# # # try:
# # #     print("Using proxy to access:", TARGET_URL)
# # #     response = opener.open(TARGET_URL)
# # #     print("Proxy response:", response.read().decode())
# # # except Exception as e:
# # #     print("Error accessing via proxy:", e)




# # import urllib.request
# # import ssl

# # # Your BrightData proxy credentials
# # PROXY_URL = 'http://brd-customer-hl_b81fbb29-zone-residential_proxy2-country-us:mpq3drhs0ama@brd.superproxy.io:33335'

# # # Target BU profile page URL
# # BU_PROFILE_URL = 'https://www.bu.edu/sph/profile/salma-abdalla/'

# # # Create an unverified SSL context (if SSL issues occur)
# # context = ssl._create_unverified_context()

# # # Configure proxy handler
# # proxy_handler = urllib.request.ProxyHandler({
# #     'http': PROXY_URL,
# #     'https': PROXY_URL
# # })

# # # Build the opener with the proxy
# # opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=context))

# # try:
# #     print("Using proxy to access:", BU_PROFILE_URL)
# #     response = opener.open(BU_PROFILE_URL)
# #     page_content = response.read().decode('utf-8')

# #     if "Salma Mohamed Hassan Abdalla" in page_content:
# #         print("Success! BU profile page loaded and profile name found.")
# #     else:
# #         print("BU profile page loaded, but profile name not found. Site may have dynamic content.")

# #     # Save page content to a file for review
# #     with open("bu_profile_test.html", "w", encoding="utf-8") as f:
# #         f.write(page_content)

# #     print("Profile page saved as 'bu_profile_test.html' for review.")

# # except Exception as e:
# #     print("Error accessing the BU profile page:", e)







# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # BrightData proxy credentials
# PROXY_URL = "http://brd-customer-hl_b81fbb29-zone-residential_proxy2-country-us:mpq3drhs0ama@brd.superproxy.io:33335"

# # BU Profile URL
# BU_PROFILE_URL = "https://www.bu.edu/sph/profile/salma-abdalla/"

# # Configure Chrome options
# chrome_options = Options()

# # Set proxy for HTTP and HTTPS
# chrome_options.add_argument(f"--proxy-server={PROXY_URL}")

# # Disable headless mode (set headless=False)
# chrome_options.headless = False

# # Additional browser settings
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--start-maximized")  # Start browser in full-screen
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--ignore-certificate-errors")

# # Initialize WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# try:
#     print("Opening BU profile page with proxy...")
#     driver.get(BU_PROFILE_URL)

#     # Allow time for the page to load fully
#     time.sleep(10)

#     # Take screenshot
#     screenshot_filename = "bu_profile_screenshot.png"
#     driver.save_screenshot(screenshot_filename)
#     print(f"Screenshot saved as {screenshot_filename}")

#     # Print profile name if available
#     profile_name_element = driver.find_element("tag name", "h1")
#     print("Profile Name Found:", profile_name_element.text)

# except Exception as e:
#     print("Error:", e)

# finally:
#     # Keep the browser open for review
#     input("Press Enter to close the browser...")

#     driver.quit()










from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from fake_useragent import UserAgent
import time

# BrightData Proxy credentials
PROXY_HOST = "brd.superproxy.io"
PROXY_PORT = "33335"
PROXY_USER = "brd-customer-hl_b81fbb29-zone-residential_proxy2-country-us"
PROXY_PASS = "mpq3drhs0ama"

# Choose proxy type (http or socks5)
PROXY_TYPE = "http"  # Change to "socks5" if http fails

# Construct proxy URL
PROXY_URL = f"{PROXY_TYPE}://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"

# BU Profile URL to test
BU_PROFILE_URL = "https://www.bu.edu/sph/profile/salma-abdalla/"

# Set up Chrome options with proxy
chrome_options = Options()
chrome_options.add_argument(f"--proxy-server={PROXY_URL}")

# Disable headless mode to visualize the browser
chrome_options.headless = False  # Set to True for headless operation

# Set up a random user-agent to bypass detection
ua = UserAgent()
user_agent = ua.random
chrome_options.add_argument(f"user-agent={user_agent}")

# Additional stealth configurations to avoid bot detection
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# Launch Selenium WebDriver with Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Apply stealth to evade detection
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

try:
    print(f"Opening BU profile page using proxy: {PROXY_URL}")
    driver.get(BU_PROFILE_URL)

    # Wait for the page to load
    time.sleep(10)

    # Screenshot for verification
    screenshot_file = "bu_profile_test.png"
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved as {screenshot_file}")

    # Extract profile name
    profile_name_element = driver.find_element("tag name", "h1")
    if profile_name_element:
        print("Profile Name Found:", profile_name_element.text)
    else:
        print("Profile name not found!")

except Exception as e:
    print("Error accessing the BU profile page:", e)

finally:
    # Keep browser open for review, press Enter to exit
    input("Press Enter to close the browser...")
    driver.quit()
