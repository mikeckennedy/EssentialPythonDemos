import json
import os


def run():
    root_path = os.path.abspath('.')
    folder = 'data'
    file = 'azure-course.json'

    filename = os.path.join(root_path, folder, file)
    print("Processing json file: " + filename)
    if os.path.exists(filename):
        print("This will probably work! File exists")
    else:
        print("Give up all hope")

    with open(filename, 'r') as fin:
        data = json.load(fin)
        engagements = data['Engagements']
        print("For the course: " + data['Name'])
        for e in engagements:
            city = e['City']
            print("The city is {0}".format(city))

        print(json.dumps(data, indent=3))
