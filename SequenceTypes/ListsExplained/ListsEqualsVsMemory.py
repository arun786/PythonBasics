number1 = [1, 2, 3]
number2 = [1, 2, 3]

if number1 == number2:
    print("Contents are the same")
else:
    print("Contents are not the same")

# the above will print Contents are the same

if number1 is number2:
    print("Lists point to the same memory")
else:
    print("Lists have different memory allocation")

    # the above will print, Lists have different memory allocation

number3 = number1

if number3 is number1:
    print("Lists point to the same memory")
else:
    print("Lists point to different memory")

# the above will print Lists point to the same memory
