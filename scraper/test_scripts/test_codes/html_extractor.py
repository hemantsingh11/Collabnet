import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://profiles.bu.edu/Nason.Hessari"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the entire HTML content
    html_content = soup.prettify()

    # Save to a file (optional)
    with open("Nason_Hessari_profile_page.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("HTML content fetched successfully!")
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)
