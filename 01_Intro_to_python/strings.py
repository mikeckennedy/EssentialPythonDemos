print("Running strings..")

s = "s1"
s = 's1'
t = "This ain't\n\t\"no walk in the park\"..."
l = "a" \
    "b" \
    "c" \
    "d"
l2 = """\
This is a literal string for
a long time
and you can keep typing...
"""
print(s)
print(t)
print(l)
print(l2)

data = dict(day="Friday", weather="raining hard!", c=102030303)

# older style
print( "Today is %s" % "Friday")

f = "Today is {day} and it is {weather} outside, but I still love {day} and count={c:,}".format(
    **data
)
print(f)