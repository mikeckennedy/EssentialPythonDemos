import json
import requests


def main():
    url = 'http://0.0.0.0:6543/api/posts/all_posts'
    resp = requests.get(url)
    print(type(resp))

    data = resp.json()
    #print(data, type(data))
    for p in data:
        print(p['title'])

    data = dict(
        title='Title of blog post from client',
        content='content',
        published='TODAY'
    )

    url = 'http://0.0.0.0:6543/api/posts/create'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    if resp.status_code != 201:
        print("Oh, that was bad: {0} -> {1}".format(
            resp.status_code, resp.text
        ))

if __name__ == '__main__':
    main()