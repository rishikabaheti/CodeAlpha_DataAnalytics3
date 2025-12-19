import requests
from bs4 import BeautifulSoup

print("Web Scraping Started")

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text
    print("Website Title:", title)
else:
    print("Failed to retrieve webpage")
