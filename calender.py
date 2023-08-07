import calendar
import datetime

def ttt():
    # get the current date
    today = datetime.date.today()

    # get the calendar for the current month
    calendar_month = calendar.monthcalendar(today.year, today.month)

    # print the calendar with the current date highlighted
    print(calendar.month_name[today.month], today.year)
    print(" Mo Tu We Th Fr Sa Su")

    for week in calendar_month:
        for day in week:
            if day == 0:
                print("   ", end="")
            elif day == today.day:
                print(f"[\033[1m{day:2d}\033[0m]", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()
