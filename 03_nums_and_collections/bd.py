import datetime

right_now = datetime.datetime.now()
print(right_now)

# ask for these values?
birth_day = datetime.date(year=2014, month=5, day=2)
this_day = datetime.date.today()

til_bd = birth_day - this_day
print( "Cool your birthday is in {0} days".format(
    til_bd.days
) )