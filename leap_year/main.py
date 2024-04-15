def leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")

leap_year(2004)