import time
import random
import undetected_chromedriver as uc

def get_stealth_driver():
    """Initialize a stealth Selenium driver in headless mode."""
    options = uc.ChromeOptions()
    options.headless = True  # Run in headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    ]
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(options=options)
    return driver

def random_delay():
    """Introduce random human-like delays to avoid detection."""
    delay = random.uniform(5, 15)
    jitter = random.uniform(0.5, 1.5)
    print(f"Sleeping for {delay + jitter:.2f} seconds...")
    time.sleep(delay + jitter)
