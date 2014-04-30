def run():
    print()
    print("All bikes")
    print()
    bikes = [
        Bike(name="Specialized FSR Comp", front_suspension="FOX Forks", rear_suspension="FOX shock + swing arm"),
        Bike(name="Specialized FSR", front_suspension="Basic Forks", rear_suspension="spring shock + swing arm"),
        Bike(name="Specialized Stump Jumper", front_suspension="Basic Forks", rear_suspension=None),
        Bike(name="Specialized Stump Jumper", front_suspension="Basic Forks", rear_suspension=None),
        Bike(name="Giant Anthem Advanced XC", front_suspension="High-end Rockshox Forks",
             rear_suspension="Rockshox shock + swing arm"),
        Bike(name="Stromer ST1 Elite", front_suspension="High-end Forks", rear_suspension=None, wattage=500),
        Bike(name="Stromer ST1", front_suspension=None, rear_suspension=None, wattage=350),
        Bike(name="Basic Walmart Bike", front_suspension="Spring Forks", rear_suspension="cheap spring + swing arm"),
    ]

    for b in bikes:
        print(b)
    print()

    electric_bikes = [
        b.name
        for b in bikes
        if b.is_electric
    ]

    print("Electric bikes: ")
    for b in electric_bikes:
        print(b)
    print()

    dual_suspension_bikes = [
        b
        for b in bikes
        if b.dual_suspension and b.rear_suspension.find("cheap") == -1
    ]

    print("Off road bikes: ")
    for b in dual_suspension_bikes:
        print(b)
    print()


class Bike:
    def __init__(self, name, front_suspension=None, rear_suspension=None, gears=21, wattage=0):
        self.wattage = wattage
        self.gears = gears
        self.name = name
        self.front_suspension = front_suspension
        self.rear_suspension = rear_suspension

    @property
    def dual_suspension(self):
        return \
            (not self.front_suspension is None and
             not self.rear_suspension is None)

    @property
    def is_electric(self):
        return not self.wattage is None and self.wattage > 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "{0}: suspension=[{1}/{2}], gears={3}, electric={4}, wattage={5}]".format(
            self.name, self.front_suspension, self.rear_suspension,
            self.gears, self.is_electric, self.wattage
        )