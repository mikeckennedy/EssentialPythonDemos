name = "Michael"#input("Wat is your name? ")
print("Hello there {0}".format(name))

# This is where we check for our friend Jeff.
if name == "Jeff" and len(name) > 2:
    print("Hi jeff")
    print("nice to see you again")
else:
    print("I don't think we have met yet {0}".format(name))

goodbye = "Cya Jeff" if name == "Jeff" else "It was nice to meet you"

print(goodbye)

for index, ch in enumerate(name):
    print("{0}. {1}".format(index, ch) )

for n in range(0, 20):
    print(n, end=",")