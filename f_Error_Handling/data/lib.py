import random


def get_days_of_week():
    days = ['mon', 'tues', 'wed',
            'thurs', 'fri', 'sat', "sun"]

    return days


def get_weather_report():
    possible_weather = [
        'sunny',
        'rainy',
        'freezing',
        'cloudy',
        'smokey'
    ]

    return random.choice(possible_weather)


def main():
    '''
    This is the coolest main method ever
    :return:
    '''
    days = get_days_of_week()

    for day in days:
        report = get_weather_report()
        #print("On {0} the weather is {1}".format(
        #    day, report
        #))

        print("On %s the weather is %s" % (day, report)
        )

    print("done")

print("My name is " + __name__)
if __name__ == "__main__":
    main()
