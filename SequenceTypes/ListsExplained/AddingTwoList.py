odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]

sum = [odd, even]
print(sum)

print()

for outer in sum:
    print(outer)
    for inner in outer:
        print(inner)
