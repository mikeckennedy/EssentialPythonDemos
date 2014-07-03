import requests

def main():
    url ='http://www.develop.com/api/course/all'

    response = requests.get(url)
    courses = response.json()
    #print(courses[0])
    #print(type(courses))

    python_courses = [
        course
        for course in courses
        if course['Name'].lower().find('python') > 0 or course['Description'].lower().find('python') > 0
    ]

    for c in python_courses:
        print(c['Name'])


if __name__ == '__main__':
    main()