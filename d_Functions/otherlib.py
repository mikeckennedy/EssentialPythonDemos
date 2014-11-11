gname = "super global thing"

def f():
    global gname
    gname = "Another global name"
    print("Global name: " + gname)
