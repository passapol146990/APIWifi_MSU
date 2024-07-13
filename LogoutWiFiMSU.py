import requests

req = requests.get('http://10.99.92.1/logout')
print(req.status_code)
print(req.url)