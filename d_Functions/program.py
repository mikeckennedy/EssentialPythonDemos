import math
import otherlib

otherlib.f()
print("After function call: " + otherlib.gname)

# from otherlib import f
# f()
# print("After function call: " + otherlib.gname)

otherlib.f.version = "1.22"
print( otherlib.f.version )


def generate_cool_numbers(limit, test=None):
    nums = []
    for n in range(1, limit):
        if not test or test(n):
            nums.append(n)

    return nums


def michael_likes_this_num(n):
    if n < 10:
        return n % 2 == 0
    else:
        return n % 20 == 2

def sort_desc_by_largest_mag(n):
    return -math.fabs(n)


for n in generate_cool_numbers(100, michael_likes_this_num):
    print("{0}".format(n), end=',')

print()
print("Try Again:")

for n in generate_cool_numbers(100, lambda x: x % 5 == 0):
    print("{0}".format(n), end=',')

print()

nums_list = [100, -199, 1,1,3,-5,8,-13,21]
nums_list.sort(key=lambda x : -math.fabs(x))
print(nums_list)








