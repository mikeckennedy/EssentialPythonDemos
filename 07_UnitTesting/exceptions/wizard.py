import time


class Wizard(object):
    def __init__(self, name):
        if not name or name.strip() == "":
            raise TypeError("Name cannot be empty")

        self.name = name
        self.mana = 2

    def cast_spell(self, target_name):
        if self.mana <= 0:
            raise OutOfManaError("Out of mana", self.name)

        self.mana -= 1

        print("The great {2} casting spell upon {0} ({1} mana remaining)"
              .format(target_name, self.mana, self.name))

    def rest(self):
        print(self.name + " is resting...")
        time.sleep(5)
        self.mana += 10


class OutOfManaError(Exception):
    def __init__(self, msg, name):
        super().__init__(msg)
        self.name = name