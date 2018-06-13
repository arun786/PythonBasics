x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

if x > y:
    print("{} is greater than {}".format(x, y))
elif x == y:
    print("{} is equal to {}".format(x, y))
else:
    print("{} is less than {}".format(x, y))
