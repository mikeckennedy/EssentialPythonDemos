class Cart(object):
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def __iter__(self):
        for item in self.__items:
            yield item


class CartItem(object):
    def __init__(self, name, price):
        self.price = price
        self.name = name

    def __str__(self):
        return "{0} at ${1:,}".format(self.name, self.price)

    def __repr__(self):
        return str(self)