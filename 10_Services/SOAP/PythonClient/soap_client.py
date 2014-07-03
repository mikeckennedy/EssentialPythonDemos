import suds

def main():
    wsdl = 'http://localhost:58483/CalculatorService.asmx?WSDL'
    client = suds.client.Client(wsdl)
    sum = client.service.Add(11, 92)
    #print(dir(client.service))

    print("The sum of 11 & 92 = {0}".format(sum))
    print("Type of sum is {0}".format(type(sum)))



if __name__ == "__main__":
    main()