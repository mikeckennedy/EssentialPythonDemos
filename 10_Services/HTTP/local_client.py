import json
import datetime

import requests


def list_posts():
    print("Listing posts:")
    r = requests.get("http://0.0.0.0:6543/api/posts")
    for p in r.json():
        print(p['title'])
    print()


def add_post():
    post = dict(title="Created by client at {0}".format(datetime.datetime.now()),
                author='app', details='from client...')
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post('http://0.0.0.0:6543/api/posts',
                      data=json.dumps(post),
                      headers=headers)

    if r.status_code != 201 and r.status_code != 200:
        raise Exception("Yikes, that hurt. Status={0}".format(r.status_code))

    print("Posted successfully with code {0} {1}".format(r.status_code, r.text))
    print()


def main():
    list_posts()
    add_post()
    list_posts()


if __name__ == '__main__':
    main()