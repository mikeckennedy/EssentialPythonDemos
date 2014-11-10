
t = 1, 2, 'orange'
print(t)

print("hi", "there")


p = ("michael", 41)

name, age = p
print("Hi {}, you're {}".format(name, age))

def get_cell():
    r = int( input("Enter row: ") )
    c = int( input("Enter col: ") )

    return r, c

cell = get_cell()

print(cell[0], cell[1])


# -----------no indexing for loop --------
people = ['jeff', 'todd', 'sarah']


for i,n in enumerate(people):
    print("{}: {} {}".format(i, n, 0))