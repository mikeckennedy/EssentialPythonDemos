import requests

url = "http://mentor.com"
resp = requests.get(url)
if resp.status_code == 200:
    print("Your web page starts with")
    print(resp.text[:1000])
else:
    print("Error {0}".format(resp.status_code))

