import random


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.mana = 3
        self.name = name

    def cast_spell(self, target_name, targets_level):

        if self.mana <= 0:
            raise OutOfManaError(self, "Out of mana")

        if targets_level > self.level:
            raise TargetTooStrongError(self, target_name, targets_level, "Target is too strong for you")

        print("The Wizard {} casts a spell upon {}".format(
            self.name, target_name
        ))
        self.mana -= 1

    def sleep(self):
        self.mana = 5
        print("The wizard sleeps and regains mana")


class WizardActionError(Exception):
    def __init__(self, wizard, msg):
        super().__init__(msg)
        self.wizard = wizard


class OutOfManaError(WizardActionError):
    pass

class TargetTooStrongError(WizardActionError):
    def __init__(self, wizard, target_name, target_level, msg):
        super().__init__(wizard, msg)
        self.target_level = target_level
        self.target_name = target_name


def main():
    targets = [
        ('cat', 2),
        ('blob', 1),
        ('tiger', 10),
        ('rabbit', 3),
    ]

    wizard = Wizard("Gandalf", 6)
    while True:
        input("Press enter to play a round")

        try:
            t = random.choice(targets)
            wizard.cast_spell(t[0], t[1])
        except OutOfManaError:
            print("Hold on....")
            wizard.sleep()
        except TargetTooStrongError as tts:
            print("Target is too strong, {} is level {} and {} is level {}, run away!".format(
                tts.wizard.name, tts.wizard.level,
                tts.target_name, tts.target_level
            ))
        except Exception:
            print("Busted?")

if __name__ == "__main__":
    main()