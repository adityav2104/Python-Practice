import requests

datta = {'Name': 'Raghav', 'Age':'24'}

response = requests.post("https://httpbin.org/post", data=datta)
print(response.status_code)
print(response.text)