import requests
from bs4 import BeautifulSoup

# IMDb URL for a specific movie (Example: Inception)
movie_url = "https://www.imdb.com/title/tt1375666/"

# Set headers to mimic a real browser
headers = {"User-Agent": "Mozilla/5.0"}

# Send a request to IMDb
response = requests.get(movie_url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract Movie Title
title = soup.find("h1").text.strip()

# Extract IMDb Rating
rating = soup.find("span", {"class": "sc-bde20123-1 cMEQkK"}).text

print(f"Title: {title}")
print(f"IMDb Rating: {rating}")
