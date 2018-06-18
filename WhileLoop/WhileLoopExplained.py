for i in range(10):
    print(i, end=' ')

print()
num = 0
while num < 10:
    print(num, end=' ')
    num += 1

print()
choosen_exits = ["east", "west", "south", "north"]
exit = ""

while exit not in choosen_exits:
    exit = input("Enter a direction")
    if exit == "quit":
        print("Game over")
        break

print("You exit")
