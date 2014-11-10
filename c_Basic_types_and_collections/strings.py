name = 'Michael'
name = "Michael"

text = "This\t\tis a\nfun string!"

text2 = """\
Exactly what is in there.

sdlfks dfs
' ssdjf lksdj fklsdlk fjsdklj f
jksdj flkjslk j

j lsk djfkj

"""

print("Before 2")
print(text2)
print("After 2")

print("Hi my name is " + name)
print(text)

for ch in text:
    print(ch, end='-')
print()
line = "Here is a line of text"

if "is" in line:
    print("Is is there")
else:
    print("no is")

index = line.find("isssssss")
print(index)

csvline = "72,21,21,50,42"

parts = csvline.split(',')
print(parts)
print(type(parts))


# --------------------------------
# Slicing

print("The slice is: '" + line[5:7] + "'")

index = len(line) - 5
print(line[index: len(line)])

print(line[-5:])
#
# sql = "SELECT * FROM Cities WHERE State ='OR'"
# cursor = execute(sql)
#
# page1 = cursor[20:30]

pth = "C:\windows\tests\new project"
print(pth)

#----------------------
# formatting

#print("Hi %s I see you are %d years old" % ('Jeff', 21))
# print("Hi {0} I see you are {1:,} years old, cool eh {0}".format(
#     'Jeff', 2100000))
# print("Hi {name} I see you are {age:,} years old, cool eh {name}".format(
#     name='Jeff', age=2100000))

data = dict(name='Ted', age=23)
data['weight'] = 180
print("Hi {name} {{name}} I see you are {age:,} years old, cool eh {name} and you weigh {weight}".format(
    **data))

print(type(data))
if 'NAME' in data:
    print("Your naem is " + data['NAME'])
else:
    print("No naem")

data2 = dict(people=[], collection="Users")
data2 = {
    'people': [],
    'collection': "Users"
}
data2['people'].append(dict(name="Jeff", age=20))
data2['people'].append(dict(name="Ted", age=34))
data2['people'].append(dict(name="Zoe", age=50))

print(data2)

for p in data2['people']:
    n = p['name']
    a = str(p['age'])
    row_len = 60 - len(n) - len(a)
    print("{0}{1}{2}".format(n, row_len*'.', a))
















