def set_year():
    year = input("Set the DEADLINE YEAR in correct format (YYYY): ")

    while not year.isdigit() or len(year) != 4:
        year = input("Set the DEADLINE YEAR in correct format (YYYY): ")

    return int(year)

def set_month():
    month = input("Set the DEADLINE MONTH in correct format (M/MM): ")

    while not month.isdigit() or len(month) not in (1,2) or int(month) < 1 or int(month) > 12:
        month = input("Set the DEADLINE MONTH in correct format (M/MM): ")

    return int(month)

def set_day(month):
    day = input("Set the DEADLINE DAY in correct format (D/DD): ")
    if month == 2:
        while not day.isdigit() or len(day) not in (1,2) or int(day) < 1 or int(day) > 28:
            day = input("Set the DEADLINE DAY in correct format (D/DD): ")
    
    elif month in (1,3,5,7,8,10,12):
        while not day.isdigit() or len(day) not in (1,2) or int(day) < 1 or int(day) > 31:
            day = input("Set the DEADLINE DAY in correct format (D/DD): ")

    elif month in (4,6,9,11):
        while not day.isdigit() or len(day) not in (1,2) or int(day) < 1 or int(day) > 30:
            day = input("Set the DEADLINE DAY in correct format (D/DD): ")

    return int(day)

def set_time():
    hour = ""
    minute = ""
    seconds = ""
    question = input("Do you want to add also DEADLINE TIME? (Yes/No): ")
    if question.lower() in ("yes","y"):
        hour = input("Set the DEADLINE HOUR in correct format (H/HH): ")
        while not hour.isdigit() or len(hour) not in (1,2) or int(hour) > 23 or int(hour) < 0:
            hour = input("Set the DEADLINE HOUR in correct format (H/HH): ")

        minute = input("Set the DEADLINE MINUTES in correct format (M/MM): ")
        while not minute.isdigit() or len(minute) not in (1,2) or int(minute) > 59 or int(minute) < 0:
            minute = input("Set the DEADLINE MINUTE in correct format (M/MM): ")

        seconds = input("Set the DEADLINE SECONDS in correct format (S/SS): ")
        while not seconds.isdigit() or len(seconds) not in (1,2) or int(seconds) > 59 or int(seconds) < 0:
            seconds = input("Set the DEADLINE SECONDS in correct format (S/SS): ")

    else:
        hour = 0
        minute = 0
        seconds = 0

        # print(int(hour),int(minute),int(seconds))
    return [int(hour),int(minute),int(seconds)]
