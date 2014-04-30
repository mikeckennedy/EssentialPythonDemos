import os

def run():

    #1. Opening a file (safely!!)
    data = []
    root_path = os.path.abspath('.')
    folder = 'data'
    file = 'Sacramentorealestatetransactions.csv'

    filename = os.path.join( root_path, folder, file)

    summary_data = dict()

    print("Loading " + filename)
    with open(filename, 'r') as fin:
        first_line = fin.readline()
        header = first_line.strip().split(',')
        for purchase in fin:
            line_data = purchase.strip().split(',')
            d = dict()
            for idx, name in enumerate(header):
                d[name] = line_data[idx]

            zip = d['zip']
            if zip in summary_data:
                t = summary_data[zip]
                n = t[0] + 1
                # assume that is rolling average
                p = t[1] * t[0]-1/t[0] + float(d['price'])/t[0]
                summary_data[zip] = (n, p)
            else:
                summary_data[zip] = (1, float(d['price']))

            data.append(d)

    data.sort(key=lambda p: -float(p['price']))

    for d in data[:5]:
        print(d)

    print("Average price for zipcode 95842 is {0} for  homes".format(
        summary_data['95842']
    ))
    print("Total zip codes are: {0}".format(len(summary_data)))


# import os
#
# def run():
#
#     #1. Opening a file (safely!!)
#     data = []
#     root_path = os.path.abspath('.')
#     folder = 'data'
#     file = 'Sacramentorealestatetransactions.csv'
#
#     filename = os.path.join( root_path, folder, file)
#     print("Loading " + filename)
#     with open(filename, 'r') as fin:
#         first_line = fin.readline()
#         header = first_line.strip().split(',')
#         for purchase in fin:
#             line_data = purchase.strip().split(',')
#             d = dict()
#             for idx, name in enumerate(header):
#                 d[name] = line_data[idx]
#
#             data.append(d)
#
#     data.sort(key=lambda p: -float(p['price']))
#
#     for d in data[:5]:
#         print(d)
#
