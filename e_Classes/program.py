from someclasses import Cat, AlleyCat


cats = [
    AlleyCat("Runaway", 1),
    Cat("Fluffy"),
    AlleyCat("Gray cat", 10),
]

acat3 = AlleyCat("Jumpy", 7)
acat3.fight_count = 27
cats.append(acat3)


acat3.age = -200

def work_with_cat(cat):
    print("New cat: {}".format(cat.__dict__))
    print("Hello there {}, you are a {}".format(
        cat.name, cat.cat_type
    ))
    cat.have_birthday()
    print("Happy birthday cat, you are {}".format(cat.age))
    if hasattr(cat, 'fight_count'):
        print("You're a tough one!" if cat.fight_count > 0 else "You're a softy")


for c in cats:
    work_with_cat(c)


print(dir(acat3))

#
#
# cat = Cat("Fluffy")
#
# print("We have created {} who is {}".format(cat.name, cat.age))
#
# cat.have_birthday()
# cat.have_birthday()
# cat.have_birthday()
# print("Now {} is {}".format(cat.name, cat.age))
#
# Cat.bad()
# Cat.bad_cls()
#
# AlleyCat.bad_cls()
#
# acat = AlleyCat("runaway", 7)
# print("We have created {} who is {}".format(acat.name, acat.age))
# acat.have_birthday()
# print("Now {} is {}".format(acat.name, acat.age))

print(dir(AlleyCat.age))

i = AlleyCat.InnerCat()
i.speak()