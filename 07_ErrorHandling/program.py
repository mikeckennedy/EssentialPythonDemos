import lib


def main():
    #lib.use_file()
    try:
        # oops, forgot: lib.init_items()
        c = lib.count_items()
        print("There are {0} items".format(c))
        lib.save_result("hello")
        return
    except lib.InvalidCallSequenceError as icse:
        print("Seems like that is out of order: {}".format(icse))
        return
    except FileNotFoundError as fnf:
        print("Sorry, file not found!")
        raise TypeError("Oops")
    except Exception as e:
        print("Sorry, that didn't work!")
    finally:
        print("Thanks for running the app, bye!")

#isinstance(e, lib.InvalidCallSequenceError)

if __name__ == "__main__":
    main()
