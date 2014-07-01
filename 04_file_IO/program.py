import json
import os
from xml.etree import ElementTree


def read_csv():
    filename = os.path.abspath(os.path.join("data", "Sacramentorealestatetransactions.csv"))
    print("CSV file is: " + filename)
    # fin = open(filename, 'r')
    with open(filename, 'r') as fin:
        header = fin.readline().strip().split(',')
        print(header)
        #print("-".join(header))
        sales = []
        for line in fin:
            parts = line.strip().split(',')
            d = dict()
            for i, val in enumerate(parts):
                key = header[i]
                d[key] = val
            sales.append(d)

        sales.sort(key=lambda s: -1 * (int(s['price'])))
        for sale in sales[:5]:
            print("{0} bed, {1} bath, sold for ${2:,}".format(
                sale['beds'], sale['baths'], int(sale['price'])
            ))


def read_xml():
    file = os.path.abspath(os.path.join('data', 'michaels_blog.xml'))
    print("Loading xml from {0}".format(file))
    dom = ElementTree.parse(file)
    print(dom.getroot())

    items = dom.findall('channel/item')
    #print(len(items))
    for post in items[:5]:
        title = post.find('title').text
        link = post.find('link').text
        print("{0} - {1}".format(title, link))



def load_elinq_course_details_from_json():
    file = os.path.abspath(os.path.join('data', 'elinq_course.json'))
    file_out = os.path.abspath(os.path.join('data', 'elinq_course_out.json'))
    print("Loading xml from {0}".format(file))

    data = None
    with open(file, 'r') as fin:
        data = json.load(fin)

    print("Data from JSON as Python object is")
    print(type(data))
    # print(data)

    course_name = data['Name']
    engagements = data['Engagements']
    print(type(engagements))
    print(course_name)
    for e in engagements:
        #if e['ActiveEngagement']:
        print(e['City'])
        e['Recommended'] = True

    with open(file_out, 'w') as fout:
        json.dump(data, fout, indent=4)


def main():
    print("-------------- CSV -------------- ")
    read_csv()
    print()
    print("-------------- XML -------------- ")
    read_xml()
    print()
    print("-------------- JSON -------------- ")
    load_elinq_course_details_from_json()
    print()


if __name__ == '__main__':
    main()