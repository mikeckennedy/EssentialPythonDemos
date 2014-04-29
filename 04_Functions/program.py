import math


def find_cool_numbers(test=None):
    nums = []
    for n in range(0, 25):
        if test is None:
            nums.append(n)
        elif test(n):
            nums.append(n)

    return nums

def even_nums(n):
    return n % 2 == 0

def thirds_nums(n):
    return n % 3 == 0

def filter_nums():
    print("Looking for some cool numbers")
    for n in find_cool_numbers(thirds_nums):
        print(n, end=',')
    print()
    print()

def sort_by_abs(n):
    return math.fabs(n)

#sort_by_abs.nickname="Chuck"

def sorting():
    some_data = [1,3,-1,7,11,-2]
    some_data.sort(key=sort_by_abs)
    print(some_data)
    some_data.sort(key=lambda n:-math.fabs(n))
    print(some_data)
#    print("Nickname: " + sort_by_abs.nickname)


def use_closures():
    c7 = create_counter(7, "The_seven")
    c100 = create_counter(100, "Biggy")

    print(c7())
    print(c7())
    print(c7())
    print(c100())

def create_counter(starting_val, name):
    def counter():
        nonlocal starting_val
        nonlocal name
        print("Incrementing {0} to {1}".format(
            name, starting_val
        ))
        starting_val+=1
        return starting_val

    return counter



def main():
    filter_nums()
    sorting()
    use_closures()


if __name__ == '__main__':
    main()