def create_greeter(name):
    has_seen = False

    def greeter_impl():
        nonlocal has_seen
        nonlocal name

        if has_seen:
            print("Nice to see you again {0}".format(name))
        else:
            print("Nice to meet you {0}".format(name))

        has_seen = True

    return greeter_impl


mgreeter = create_greeter("Michael")
jgreeter = create_greeter("Jeff")

mgreeter()  # nice meet
mgreeter()  # hi again
mgreeter()  # hi again
jgreeter()  # nice to meet
mgreeter()
jgreeter()














