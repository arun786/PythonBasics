year = int(input("Enter a year"))

if 1 > year > 9999:
    print("Invalid year")
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
