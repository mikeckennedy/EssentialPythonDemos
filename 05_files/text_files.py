import os


lines_parsed = 0
def parse_by_line(fin, header):
    global lines_parsed
    for l in fin:
        if l:
            lines_parsed += 1
            print("Processing line: " + l)
            cols = l.split(',')
            d = dict()
            for index, val in enumerate(cols):
                d[header[index]] = val
            yield d
  
def run():
    #root_folder = os.path.dirname(__file__)
    root_folder = os.path.abspath('.')
    filename = os.path.join(root_folder, 'data', 'Sacramentorealestatetransactions.csv')
    print("Opening file:")
    print(filename)

    header = None
    with open(filename, 'r') as fin:
        header = fin.readline().split(',')
        print(header)
        data = parse_by_line(fin, header)

        prices = (
            get_price_from_row(h)  # select
            for h in data  # from
            if h['beds'] == '2'  # where
        )
        #prices = list(prices)
        # counter_dict = dict()
        # fin.seek(0)
        # for sale in parse_by_line(fin, header):
        #     key = sale['zip']
        #     if key in counter_dict:
        #         counter_dict[key] += 1
        #     else:
        #         counter_dict[key] = 1
        # print(counter_dict)

        data2 = []
        for p in prices:
            if len(data2) >= 10:
                break
            data2.append(p)

        total_exchange = sum(data2)
        ave_sale = total_exchange / len(data2)

        print("Average sale price: ${0:,}".format(ave_sale))
        global total_count
        global lines_parsed
        print("Looped {0} times".format(total_count))
        print("Parsed file lines {0} times".format(lines_parsed))


total_count = 0


def get_price_from_row(sale_row):
    global total_count
    total_count += 1
    return float(sale_row['price'])
