def get_fibonacci_numbers():
    # 1, 1, 2, 3, 5, 8, 13, 21,
    current, nxt = 0,1
    #data = []
    while True:
        current, nxt = nxt, nxt+current
        #data.append(current)
        yield current


def some_test(n):
    return n > 20000


def run():
    f = get_fibonacci_numbers()
    for n in f:
        if some_test(n):
            break

        print(n, end=',')

    print()
    print("done")
