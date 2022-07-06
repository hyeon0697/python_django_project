import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(
    endpoint, params={"abc": 123}, json={"title": "abc123", "content": "Hello world", "price": "abc123"})  # HTTP Get Request
# API -> Method, Application programing interface
# Phone -> Camera -> App -> Api -> Camera
# REST APIs -> Web Api
# HTTP Request
# print(get_response.headers)
# print(get_response.text)  # print raw text response
# HTTP Requset -> HTML, REST API HTTP Request -> JSON

# JavaScript Object Nototion ~ Python Dict
print(get_response.json())
print(get_response.status_code)
