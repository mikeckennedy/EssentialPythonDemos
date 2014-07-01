from exceptions.wizard import Wizard, OutOfManaError


def main():
    wizard = Wizard("Zorax")

    while True:
        cmd = input("What do you want to do now, (a)ttack or (r)est? ")
        try:
            if cmd == 'a':
                target = input("What do you want to attack? ")
                wizard.cast_spell(target)
            elif cmd == 'r':
                wizard.rest()
            else:
                print("Don't know what to do with " + cmd)
        except OutOfManaError as oome:
            print("You are out of mana, you MUST REST NOW!")
            print("It was {0} who caused this".format(oome.name))
        except Exception as x:
            print("Yikes! That failed, try again: {0}".format(x))


if __name__ == '__main__':
    main()