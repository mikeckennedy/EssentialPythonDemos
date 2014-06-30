import datetime


class Cat(object):
    def __init__(self, name, friskiness=50):
        self.__friskiness = friskiness
        self.name = name
        self.__birthday = datetime.datetime.now()
        self._semi_hidden = "hide me"

    def play(self):
        if self.__friskiness > 20:
            print("{0} jumps around playfully!".format(self.name))
        else:
            print("{0} rolls over".fromat(self.name))

    @property
    def friskiness(self):
        return self.__friskiness

class Dog():
    def __init__(self, **kwargs):
        for k in kwargs:
            self.__dict__[k] = kwargs[k]

d = {}
dog = Dog(name="Rover", age=7, friskiness=92)

print("Details of dog")
print(dir(dog))



cat = Cat("fluffy")
print(dir(cat))

#print(str(cat.__birthday))
print("Friskiness level = {0}".format(cat.friskiness))
cat.play()