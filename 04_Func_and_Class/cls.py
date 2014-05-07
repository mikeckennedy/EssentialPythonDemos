
class Animal(object):

    def __init__(self, age, species):
        self.species = species
        self.__age = age

    def __str__(self):
        return "{0} is {1} years old".format(self.species, self.__age)

    def __repr__(self):
        return str(self)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,val):
        if val < 0:
            raise TypeError("Invalid age, must be positive")

        self.__age = val


class Pet(Animal):
    def __init__(self, age, species, is_indoor_only):
        super().__init__(age, species)
        self.is_indoor_only = is_indoor_only

    def play(self):
        print(
            "INDOOR " if self.is_indoor_only else "OUTDOOR " +
            self.species + " is playing!" )


tiger = Animal(2, "Tiger")
cat = Pet(12, "House Cat", False)
print(tiger.age)
tiger.age += -1
print([tiger])

cat.play()














