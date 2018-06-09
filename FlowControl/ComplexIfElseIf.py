age = int(input("Enter your age : "))
if (age > 15) and (age < 65):
    print("Have a good day at work")
else:
    print("Please enjoy your free time")

if 15 < age < 65:
    print("Have a good day at work")
else:
    print("Please enjoy your free time")

age = int(input("Please enter the age again"))
if (age < 16) or (age > 64):
    print("Please enjoy your free time")
else:
    print("Have a good day at work")
