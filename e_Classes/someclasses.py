class Cat(object):
    # static (sorta)
    # id = 1

    def __init__(self, name):
        self.name = name
        # self.__dict__['name'] = name
        self.__age = 1
        self.friskiness = 20
        self.cat_type = "Basic cat"

    @property:
    def age(self):
        print("Getting age for {}".format(self.name))
        return self.__age

    @age.setter
    def age(self, val):
        if val < 0:
            val = 0

        self.__age = val

    def have_birthday(self):
        self.__age += 1

    @staticmethod
    def bad():
        print("Cats are bad, get a dog!")

    @classmethod
    def bad_cls(cls):
        print("Cats are bad, get a dog! From: {}".format(cls))


class AlleyCat(Cat):
    def __init__(self, name, shagginess):
        super().__init__(name)
        self.shagginess = shagginess
        self.cat_type = "Alley cat"
        self.fight_count = 0

    def have_birthday(self):
        super().have_birthday()
        self.age += 8

    # def have_birthday(self):
    #     self.age += 5

    class InnerCat:
        def speak(self):
            print("I am the inner cat")



class Dog:
    pass


class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)


