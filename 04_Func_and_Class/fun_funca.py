import random
import math


def show_cool_nums(limit, test=None):
    for n in range(0, limit - 1):
        if test and test(n):
            print(n, end=' ')


def get_rand_num(limit, sequence, *args, **kwargs):
    print("other args are {0} and keyword arguments={1}".format(args, kwargs))
    return random.randint(0, limit)


def main():
    nxt = get_rand_num(10, 1, 1, 2, 7, format_key=2, indent_level=7)
    print("The number is {}".format(nxt))
    eq_class = 3  # uses lambda as a closure
    show_cool_nums(20, lambda n: n % 4 == eq_class)

    print("fib nums to 10")
    for n in get_fib_nums():
        if n > 20000:
            break
        print(n, end=', ')


def get_fib_nums():
    # 1,1,2,3,5,8,...
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current+ nxt
        # bad! data.append(current)
        yield current

#
# def evens(n):
#     return n % 2 == 0
#
# def abs_reverse_sort(n):
#     return -math.fabs(n)

lst = [1, 1, -3, 7, -2, 200, -1]
lst.sort(key=lambda n: math.fabs(n))
print(lst)

if __name__ == '__main__':
    r = main()
    #print(type(r))