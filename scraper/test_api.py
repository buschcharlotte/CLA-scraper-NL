import requests

url = "https://cao.minszw.nl/mozard/!suite16.getObjectRegels"

params = {
    "mObjecten": ",37033",
    "mSelod": "877732"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.headers.get("content-type"))
print(response.text[:1000])