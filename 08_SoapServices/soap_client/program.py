import suds

def main():
    wsdl_url = "http://localhost:52513/CalculatorService.asmx?WSDL"
    c = suds.client.Client(wsdl_url)

    #print(c)
    x = input("Enter first number: ")
    y = input("Enter second number: ")

    add = c.service.Add(x, y)
    sub = c.service.Subtract(x, y)

    print("Cool, the sum is {} and diff is {}".format(add, sub))


if __name__ == "__main__":
    main()