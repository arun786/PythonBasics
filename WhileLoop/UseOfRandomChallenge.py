import random

highest = 100
answer = random.randint(1, highest)

print(answer)

guess = 0
while answer != guess:
    print("Please guess the number..")
    guess = int(input())
    if guess == 0:
        break;
    elif answer < guess:
        print("Please enter a lower number...")
    elif answer > guess:
        print("Please enter a higher number...")
    else:
        print("You answered correctly")
