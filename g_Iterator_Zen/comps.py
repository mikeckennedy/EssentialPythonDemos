# working data for the next few examples

class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

people = [
    Person("Jeff", 42, ['tennis', 'hockey', 'football']),
    Person("Michael", 40, ['biking', 'hiking', 'motocross']),
    Person("Pierre", 39, ['biking', 'kite boarding']),
    Person("Stacey", 32, ['skiing']),
]


def ping():
    print('ping')
    return True


#  bikers = [
#     p.name.upper() # projection / selection
#     for p in people # from TABLE
#     if 'biking' in p.hobbies # where hobby is biking
# ]
#
# print(bikers, type(bikers))

bikers = (
    p.name.upper() # projection / selection
    for p in people # from TABLE
    if ping() and 'biking' in p.hobbies # where hobby is biking
)

print(bikers, type(bikers))

for b in bikers:
    print('pong')
    print(b)