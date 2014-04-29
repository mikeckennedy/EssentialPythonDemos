
import requests

r = requests.get('http://esri.com')
print('There are {0:,} characters on the home page'.format(
    len(r.text)
))