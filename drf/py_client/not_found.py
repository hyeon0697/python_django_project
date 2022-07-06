import requests


endpoint = "http://localhost:8000/api/products/699941321351365/"


get_response = requests.get(endpoint)
print(get_response.json())
