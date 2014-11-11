import os
import io_helper
import random

def count_lines(name):
    filename = os.path.join("data", name + ".py")

    return io_helper.count_lines(filename)


def some_io_function(name):

    if random.randint(1, 5) == 1:
        raise NotImplementedError("Not today!")

    filename = os.path.join("data", name + ".py")

    return io_helper.count_chars(filename)
