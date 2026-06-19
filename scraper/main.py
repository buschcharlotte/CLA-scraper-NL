import requests
from bs4 import BeautifulSoup

url = "https://cao.minszw.nl/mozard/!suite16.scherm1168?mSelod=654165"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for a in soup.find_all("a"):
    tekst = a.get_text(" ", strip=True)

    if tekst:
        print(tekst[:120])
        print("Lengte HTML:", len(response.text))
        