import requests


def main():
    url = input("Please enter the URL to start searching: ")

    response = requests.get(url)

    html = response.text.lower()

    while True:
        word = input("What do you want to find (one word please)? ")
        word = word.strip().lower()
        index = html.find(word)
        if index >= 0:
            print("Found {0}\n{1}".format(
                word,
                html[index-50:index+100]
            ))



if __name__ == "__main__":
    main()