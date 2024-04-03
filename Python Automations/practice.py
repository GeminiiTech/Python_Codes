import requests

url = "https://geminitech.onrender.com/"
response = requests.get(url)

data = response.json()

print(data)