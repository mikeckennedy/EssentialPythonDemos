# import sys
#
# def conditional_importer():
# import requests
# r = requests.get("http://develop.com")
# print(r.status_code)
#
# conditional_importer()
#
# r2 = requests.get("http://develop.com")
# print(r2.status_code)

def long_method(arg1, arg2, arg3, arg4, argument5,
                argument6, argument7, argument8,
                argument9, argument10):
    pass


lst = [
    n * n
    for n in {1, 2, 5, 11}
    if not n % 2 == 0
]

text = ("Some text is here" +
        "And more text" +
        "Some text is here")

print(text)

if True:
    print("line 1")
    print("line 2")


def func1():
    pass


def func2():
    pass


print("Testing for none...")

text = 'true'  # input('Should it be None? true, false')
data = None if text == "true" else "THis is not none"

if data is None:
    print("Oh, you made it none")
else:
    print("Nice, you made it not none")

seq1 = None
seq2 = []
seq3 = [1, 2]


def test_seq(s):
    if s:
        print("Sequence is true: " + str(s))
    else:
        print("Sequence is FALSE: " + str(s))


test_seq(seq2)
test_seq(seq3)
test_seq(seq1)

print("Some non-pythonic code...")

# data = [1,1,2,3,5,8]
# for (int i=0; i< len(data); i++) {
# d = data[i]
# print(d*d)
# }

print("Not so pythonic")
data = [1, 1, 2,3, 5, 8]
for i in range(0, len(data)):
    d = data[i]
    print("{0}th square is {1}".format(i + 1, d * d))

print("better")

data = [1, 1, 2, 3, 5, 8]
for i, d in enumerate(data):
    print("{0}th square is {1}".format(i + 1, d * d))