import custom_iter
import generators
import comprehensions


def main():
    try:
        custom_iter.run()
        generators.run()
        comprehensions.run()
    except Exception as x:
        print("ERROR: SOMETHING IS WRONG: {0}".format(x))
        raise


if __name__ == "__main__":
    main()
