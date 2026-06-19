import requests
from bs4 import BeautifulSoup

url = "https://cao.minszw.nl"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

print("Aantal links:", len(links))

for link in links[:20]:
    print(link.get("href"))

 ##########################################################

    import requests
from bs4 import BeautifulSoup

url = "https://cao.minszw.nl/mozard/!suite86.scherm0325?mPag=991"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    tekst = link.get_text(strip=True)
    href = link.get("href")

    if tekst:
        print(tekst, "->", href)

##########################################################

import requests
from bs4 import BeautifulSoup

url = "https://cao.minszw.nl/mozard/!suite16.scherm1168?mSelod=654165"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Aantal formulieren:", len(soup.find_all("form")))
print("Aantal tabellen:", len(soup.find_all("table")))

print("\n=== TITEL ===")
print(soup.title.text)

print("\n=== FORMULIEREN ===")
for form in soup.find_all("form"):
    print(form.get("action"))