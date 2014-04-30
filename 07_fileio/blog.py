import requests
from xml.etree import ElementTree

def run():
    url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
        #'http://feeds.arstechnica.com/arstechnica/index/'#input("Enter url for RSS: ")
    r = requests.get(url)
    xml_text = r.text

    dom = ElementTree.fromstring(xml_text)

    items = dom.findall('channel/item')
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        print('{0} at {1}'.format(title, link))