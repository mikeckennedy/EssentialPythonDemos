def get_numbers(start, end, test=None):
    nums = []
    for n in range(start, end):
        if test is None or test(n):
            nums.append(n)
    return nums


def main():
    for n in get_numbers(5, 100, lambda x: x % 5 == 0):
        print(n, end=",")


# def is_even(n):
#     return n % 2 == 0




if __name__ == '__main__':
    main()