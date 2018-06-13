name = input("Please enter name of the person")
age = int(input("Please enter age of the person"))

if (18 < age < 31):
    print("{} Welcome to the holiday".format(name))
else:
    if (age > 31):
        print("sorry {}, you are overage".format(name))
    else:
        print("{}, please come after {} years".format(name, 18 - age))
