import requests
url = "https://catfact.nina/fact"
response = requests.get(url)
if response.status_code == 200:
  data = response.json()
  print("Random cat fact:", data["fact"])
else:
print("Error:", response.status_code)
