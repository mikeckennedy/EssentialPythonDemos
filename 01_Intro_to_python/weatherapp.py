import random


def get_days_of_week():
    days_list = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    return days_list


def get_weather_report(day):
    possible_reports = ['Sunny', 'Snowing', 'Raining', 'Hot', 'Cold', 'Smokey']
    return random.choice(possible_reports)


def main():
    days = get_days_of_week()

    for d in days:
        report = get_weather_report(d)
        print("The weather on {0} is {1}.".format(
            d, report
        ))


if __name__ == '__main__':
    main()