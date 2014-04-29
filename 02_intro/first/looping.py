from program import *

nums = [1,1,2,3,5,8,13,21]
for (idx, val) in enumerate(nums):
    print("The {0}nth number is {1}".format(idx, val))


print("First 50 even numbers")
for n in range(0, 51):
    if n % 2 == 0:
        print(n, end=',')

print()
print("Days of the week")
for d in get_days_of_week():
    print(d)