text = input("Enter some text...")
if text:
    print("You entered text {}".format(text))
else:
    print("You did not enter any text")

age = int(input("Enter your age"))
if not (age < 18):
    print("you are old enough to vote")
else:
    print("come back after {}".format(18 - age))
