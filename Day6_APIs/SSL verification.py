# import requests module
import requests

# Making a get request
response = requests.get('https://expired.badssl.com/', verify = False)

# print request object
print(response.status_code)