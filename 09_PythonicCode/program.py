"""
This is just the main program.
"""

import comprehensions
import nums
from shopping import ShoppingCart, CartItem


def main():
    """
    This is the main method
    """
    cart = ShoppingCart(42)
    cart.add(CartItem("Telsa", 120000))
    cart.add(CartItem("Lotus", 79000))

    print("Cart summary:")
    for item in cart:
        print("{0} for ${1:,}".format(item.name, item.price))

    print("Total price ${0:,}".format(
        cart.total_price
    ))

    nums.run()

    comprehensions.Run(42)
    comprehensions.run2() #NO! u = comprehensions.run2()


if __name__ == "__main__":
    main()
