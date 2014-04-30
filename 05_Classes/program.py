from animals import Zebra
from shopping import ShoppingCart, CartItem


def main():
    cart = ShoppingCart(42)
    cart.add(CartItem("Telsa", 120000))
    cart.add(CartItem("Lotus", 79000))
    cart._semiprivate = 2

    print("Total is ${0:,}.".format(cart.total_price))
    print("Customer id is {}".format(cart.customer_id))
    cart.customer_id = 30
    print("Customer id is {}".format(cart.customer_id))
    #cart.customer_id = -1
    #cart.__items.clear()
    #print( dir(cart) )
    print(cart)
    l = [cart, cart]
    print(l)

    print()
    print()

    z = Zebra("Hippotigris", 11)
    z.run()


if __name__ == "__main__":
    main()