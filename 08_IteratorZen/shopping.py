class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


class ShoppingCart:
    def __init__(self, customer_id):

        if customer_id <= 0:
            raise Exception("Error")

        self.__items = []
        self.__customer_id = customer_id
        self._semiprivate = 1

    def add(self, item):
        self.__items.append(item)

    @property
    def total_price(self):
        total = 0
        for item in self.__items:
            total += item.price
        return total

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, val):
        if val <= 0:
            raise Exception("Error")

        self.__customer_id = val

    def __str__(self):
        return "Cart with {0} items, total ${1:,}.".format(
            len(self.__items), self.total_price
        )

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        #return self.__items.__iter__()
        for item in self.__items:
            yield item







