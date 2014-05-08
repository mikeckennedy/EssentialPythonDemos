items = None


def init_items():
    global  items
    items = [1, 2, 3]


def count_items():
    global items
    if items is None:
        raise InvalidCallSequenceError("You must first call init_items")
    return len(items)


def save_result(param):
    return None

def use_file():

    # this is kind of with:

    fin = open('somefile.txt', 'w')
    try:
        try:
            pass
        finally:
            pass
        fin.write("this is good")
        raise Exception("boo!")
    finally:
        print('closing file...')
        fin.close()

    with open('somefile.txt', 'r') as fin2:
        print(fin2.read())



class InvalidCallSequenceError(Exception):
    def __init__(self, msg):
        super().__init__(msg)