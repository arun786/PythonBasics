name = input("please enter the name of the person : ")
age = int(input("How old are you {} ? ".format(name)))
if (age >= 18):
    print("You are old enough to vote.")
    print("please start voting")
else:
    print("please come back after {} years ".format(18 - age))
