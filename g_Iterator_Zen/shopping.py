
class Cart:
    def __init__(self):
        self.__items = []

    def add(self, item):
        if not item:
            raise TypeError("Can't be null")

        self.__items.append(item)

    # def __iter__(self):
    #     i = self.__items.__iter__()
    #     # print(dir(i))
    #     return i

    def __iter__(self):
        for i in self.__items:
            print("............... returning item " + i.name)
            yield i


class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price