print("Enter a number in between 1 and 10")
guess = int(input())

if (guess < 5):
    print("Please enter a higher value")
    guess = int(input())
    if (guess == 5):
        print("You have guessed it right")
    else:
        print("Sorry you are wrong")
elif (guess > 5):
    print("Please enter a lower value")
    guess = int(input())
    if (guess == 5):
        print("You have guessed it right")
    else:
        print("Sorry you are wrong")
else:
    print("You are right the first time")

# the above code had duplication, lets improve it

print("Please enter again for better code")
guess = int(input())

if (guess != 5):
    if (guess > 5):
        print("Please guess it lower")
    else:
        print("Please guess it higher")

    guess = int(input())

    if (guess == 5):
        print("you guessed it right")
    else:
        print("Sorry you are wrong")
else:
    print("You guessed it correct the first time")
