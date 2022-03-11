import requests

# url = "https://www.naver.com"
# url = 'http://localhost:8000/api/greet?name=dong&age=30'
url = 'http://localhost:8000/api/sensor?sensor=temp'
response = requests.get(url)
print("status code :", response.status_code)
# print(response.text)
print(response.json())



