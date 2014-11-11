class AnonObject(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__


txt = "jeff-7, ralph-10, sarah-20"

peoplesText = txt.split(',')
people = []

for pt in peoplesText:
    parts = pt.strip().split('-')
    print(parts)

    d = AnonObject()
    d.name = parts[0]
    d.age = parts[1]

    people.append(d)

print(people)

for p in people:
    print(p.name)
    p.name = 'Ted'


