import requests

url = 'http://localhost:5000/api/answer'
files = {'file': open('test.py', 'rb')}
r = requests.post(url, files=files)
print(r.json())