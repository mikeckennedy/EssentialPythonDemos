class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

def run():
    people = [
        Person("Jeff", 42, ['tennis', 'hockey', 'football']),
        Person("Michael", 40, ['biking', 'hiking', 'motocross']),
        Person("Pierre", 39, ['biking', 'kite boarding']),
        Person("Stacey", 32, ['skiing']),
    ]

    bikers = [
        dict(BigName=p.name.upper(), RealAge=p.age) # select / project / transform
        for p in people # data source, e.g. table
        if 'biking' in p.hobbies
    ]

    bikers_gen = (
        dict(BigName=p.name.upper(), RealAge=p.age) # select / project / transform
        for p in people # data source, e.g. table
        if 'biking' in p.hobbies
    )

    print(type(bikers))
    print(type(bikers_gen))

    for n in bikers_gen:
        print(n)


















