
def run():
    cart = ShoppingCart()

    cart.add(CartItem("Tesla P85 - Yellow", 120000))
    cart.add(CartItem("Tesla - White", 69000))
    cart.add(CartItem("Lotus Evora", 79890))

    print_cart_summary(cart)


def print_cart_summary(cart):
    print()
    print("Shopping cart details:")
    print()
    subtotal = 0

    # TODO: Make sure cart is iterable.
    for item in cart:
        print("{0} ${1:,}".format(
            (item.name + " ").ljust(50, '.'),
            item.price))
        subtotal += item.price

    print("".ljust(60, '_'))
    print("{0} ${1:,}".format("Subtotal".ljust(50), subtotal))
    print("{0} ${1:,}".format("Tax".ljust(50), int(subtotal*.15)))
    print("{0} ${1:,}".format("Total".ljust(50), int(subtotal*1.15)))



class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


class ShoppingCart:
    def __init__(self):
        self.__items = []

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