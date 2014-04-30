
class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("The animal is running...")


class Zebra(Animal):

    def __init__(self, name, stripiness):
        super().__init__(name)
        self.stripiness = stripiness

    def run(self):
        super().run()
        print("The zebra (with stripe factor {1}, known as {0}) gallops!"
        .format(self.name, self.stripiness))


