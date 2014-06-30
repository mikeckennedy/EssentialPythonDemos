import cart
import person

def fib_numbers():
    nxt, current = 1, 0
    while True:
        current, nxt = nxt, nxt + current
        yield current

# def fib_numbers(count):
#     numbers = []
#     # 1,1,2,3,5,8...
#     nxt, current = 1, 0
#     while len(numbers)< count:
#         current, nxt = nxt, nxt + current
#         numbers.append(current)
#
#     return numbers


def main():
    my_cart = cart.Cart()
    my_cart.add(cart.CartItem("Tesla", 120000))
    my_cart.add(cart.CartItem("Lotus", 78000))
    my_cart.add(cart.CartItem("Van", 18000))

    for item in my_cart:
        print(item)

    print()
    print("Fib numbers")
    for n in fib_numbers():
        if n > 10000:
            break

        print(n, end=',')
    print()

    print()
    print("Comprehensions")

    bikers = (
        (p.age, p.name) # select
        for p in person.people # from
        if test(p, "bikers") and 'biking' in p.hobbies
    )

    biker_ages = (
        p[0]
        for p in bikers
        if test(p, "ages")
    )

    lst = list(biker_ages)
    lst.sort()
    youngest = lst[0]
    print(youngest)

    print(type(bikers))
    print(bikers)


def test(item, loc):
    print("testing item " + str(item) + ' at ' + loc)
    return True

if __name__ == '__main__':
    main()