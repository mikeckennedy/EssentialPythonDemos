import datetime

num_text = 7  #input("What is your favorite numbers?")
n = int(num_text)
print("The next one is {0:,}".format(n + 1))
print("The num is %d" % n)

t = """\
multi line strings
are sometimes fun too!
"""

print(t.index('too'))

d = dict(name='jeff', age=27)
txt = "Hi {name} I see that you are {age} years old!".format(
    **d  #name='ted', age=7
)
print("=" * len(txt))
print(txt)

dt = datetime.timedelta(days=7)
next_meeting = datetime.datetime.now() + dt
print("Next meeting is at {0}".format(next_meeting))

data = []
print(type(data))
print(dir(data))

data.append(1)
data.append(2)
data.append(7)
data.extend([3, 3, 4])
# data1+data2
print(data)

d = {
    'name': 'jeff',
    'age': 7
}

print(d)
print('name' in d)
print(d['name'])
# print( 'name3' in d)
# print(d['name3'])

d2 = dict(name="Jeff", age=33, hobby="Running")
print(d2)

d2['name'] = "Ted"

s = {1, 1, 1, 2, 3, 2}
print(s)

t = (1, 2, 3, 2)
print(t[2])
t = 7,
print(t, type(t))












