
data = []
data.append(7)
data.append(8)
data.extend([1,2,3])
data.append(1)
data.append(1)
#data.sort()

print(data)
#data.remove(1)
del data[4]
print(data)

print("Index of {0} is {1}".format(
    1,
    data.index(1)
))

num = int(input("What number to look for? "))
if num in data: # NO: data.index(num)>= 0:
    print("Yes")
else:
    print("No")

print(data)