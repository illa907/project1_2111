import requests

response = requests.get("https://httpbin.org/get")
print(response.content)
print(response.text)
print(f"Data type - {type(response.content)}")
print(f"Data type - {type(response.text)}")