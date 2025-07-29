
#GET METHOD
import requests

response = requests.get("https://api.github.com/users/adityav2104")
print(response)
print(response.content)


#WITH AUTHENTICATION
from requests.auth import HTTPBasicAuth

response = requests.get(
    'https://api.github.com/users',
    auth=HTTPBasicAuth('adityav2104', 'Aditya21@#')
)

print(response.status_code)
print(response.text)