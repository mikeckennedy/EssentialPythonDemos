import random


def main():
    days = get_days_of_week()

    # Let's get the report for each day.
    for day in days:
        report = get_random_weather_report()
        text = None
        #print("THe length of text is {0} {1}".format(len(text)))
        if day == 'sat' or day == 'sun':
            text = "Lovey weekend day on {0}: {1}".format(day, report)
        else:
            text = ("The weather on {0} will be {1}.".
                    format(day, report) )
        print(text)

def get_days_of_week():
    """
    This will return all the days of the week starting with Monday.
    """
    return ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']


def get_random_weather_report():
    reports = ['sunny', 'hot', 'dusty', 'windy', 'smoggy', 'rainy']
    index = random.randint(0, len(reports) - 1)
    return reports[index]


if __name__ == '__main__':
    main()
