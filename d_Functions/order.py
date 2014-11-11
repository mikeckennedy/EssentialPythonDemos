
def m2():
    print("M2")

def pos(x, y, w="hey", z=5, *args, **kwargs):
    # dict(name="ted", age=40)
    print(x, y, w, z, args, kwargs)

def m1():
    print("M1")
    m2()
    m3()
    pos(1,2,3,4,7, 11, name="ted", age=40, hobbie='running')

# m1() <-- no, would fail (m3 missing)

def m3():
    print("M3")


if __name__ == "__main__":
    m1()

