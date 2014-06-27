lst = [1, 1, 2, 3, 5, 8, 13]
st = {1, 1, 2, 3, 5, 8, 13}

d = {
    "name": "Michael",
    "age": 41
}
d = dict(name="Michael", age=41)

print(d, type(d))

print(lst)
print(st)

print(lst[2])
print(lst[-1])
print(lst[len(lst) - 1])  # bad!!

# slice a list...
print(lst[:3])
print(lst[-3:])
print(lst[2:5])

lst.append(21)
print(lst)
#lst.append([7, 7, 2, 5])
lst.extend([7, 7, 2, 5])
print(lst)

lst.remove(7)
print(lst)

del lst[6]
print(lst)

#d['hobby']='motocross'

hobby = "nothing"
if "hobby" in d:
    hobby = d['hobby']

print("Dictionary: name={0}, hobby={1}".format(
    d['name'],hobby))