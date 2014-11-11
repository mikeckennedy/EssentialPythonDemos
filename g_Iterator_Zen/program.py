from g_Iterator_Zen.shopping import Cart, CartItem

cart = Cart()

cart.add( CartItem('Pumpkin Pie', 2.99) )
cart.add( CartItem('Sandwich', 5.99) )
cart.add( CartItem('Cranberry Rasb Drink', 7.99) )

total = 0.0
for item in cart:
    print("Computing price from " + item.name)
    total += item.price

print("The final price is ${0:,}".format(total))