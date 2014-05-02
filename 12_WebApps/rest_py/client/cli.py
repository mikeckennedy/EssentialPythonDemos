import datetime
import json
import requests

url = 'http://0.0.0.0:6544/api/posts'
#urlp = 'http://0.0.0.0:6544/api/posts/create'

resp = requests.get(url)
data = resp.json()
#print(data, type(data))

for p in data:
    print(p['title'])

title = input("What do you want to post about today? ")

new_post = dict(title=title, pub=str(datetime.datetime.now()))
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
resp = requests.post(url, data = json.dumps(new_post), headers=headers)

#print(dir(resp))
print("Was that OK? {0}".format(resp.status_code == 201))

resp = requests.get(url)
data = resp.json()
#print(data, type(data))

for p in data:
    print(p['title'])