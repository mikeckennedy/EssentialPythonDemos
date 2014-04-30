import random
import tree as tree_module


def run():
    print()
    print()
    print("Some (efficient) information about fibonacci numbers:")
    print()
    fib = get_fibonacci()

    sum_total = 0
    for n in fib:
        if n >= 100000:
            break
        sum_total += n
        print(n, end=',')
    print()

    print("Sum of fib less than 100,000 => {0:,}".format(sum_total))
    print()
    print()

    tree = tree_module.Tree()

    for n in range(10):
        tree.insert(random.randint(0, 100))
    print("Here is a ordered tree (raw):")
    print(tree)
    print()
    print("This might make more sense (in order):")
    for n in tree:
        print(n, end=',')
    print()
    print()


def get_fibonacci():
    current, nxt = 1, 1
    while True:
        yield current
        current, nxt = nxt, nxt + current
