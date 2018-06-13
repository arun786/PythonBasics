for state in ["maharastra", "meghalaya", "assam", "arizona"]:
    print("I stayed in {}".format(state))

# steps in for loop
for i in range(0, 10, 2):
    print(i, end=' ')

print()

for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i * j))
    print("------------------")
