import requests

session = requests.Session()

start_url = "https://cao.minszw.nl/mozard/!suite16.scherm1168?mSelod=654165"

r = session.get(start_url)

print("Status start:", r.status_code)
print("Cookies:", session.cookies.get_dict())