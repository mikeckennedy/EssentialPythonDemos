import subprocess
import calculator

def main():
    subprocess.call("notepad.exe")
    print("Working with calc v{0}".format(calculator.version))
    g = calculator.graphing.Graph()
    g.show()
    calc = calculator.ScientificCalculator()

    print("Sum of {0} and {1} is {2}".format(
          1,2, calc.add(1,2)))

    print(calc.is_finite(2310498129084290384))


if __name__ == "__main__":
    main()