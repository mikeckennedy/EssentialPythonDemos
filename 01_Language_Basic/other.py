import unittest


def method():
    print("I am other")


#print("The name of other.py currently is {}".format(__name__))
def show_title():
    print("Looks like you want to run me!")


def show_suffix():
    pass


if __name__ == '__main__':
    show_title()
    method()
    show_suffix()


class Tests(unittest.TestCase):
    pass
#sql = "SELECT * FROM Books WHERE title"