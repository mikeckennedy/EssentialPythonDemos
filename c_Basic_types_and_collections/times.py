import datetime

t0 = datetime.date.today()
t00 = datetime.datetime(year=2012, month=1, day=1)
t1 = datetime.datetime.now()
print("Today is {0}".format(t1))
print("The hour is {0}".format(t1.hour))

dt = t1 - t00
print(dt)

nums = [1, 2]
nums += [3, 4]
print(nums)