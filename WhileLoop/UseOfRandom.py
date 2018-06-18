import random

highest = 100
answer = random.randint(1, highest)
print(answer)

print("Guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess a number higher number")
    else:
        print("Guess a lower number")
    guess = int(input())
    if guess == answer:
        print("You guess it right")
    else:
        print("sorry dude")
else:
    print("You guessed the right answer")
