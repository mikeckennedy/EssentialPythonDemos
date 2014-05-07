import json
import os


def run():

    f = os.path.join('.', 'data', 'azure.json')
    with open(f, 'r') as fin:
        data = json.load(fin)
        print("The course {0} has the url {1}".format(
            data['Name'], data['UrlPath']
        ))
