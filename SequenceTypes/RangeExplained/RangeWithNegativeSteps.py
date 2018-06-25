start = 1
stop = 10
step = 2

number = range(start, stop, step)

for i in number:
    print(i, end=" ")
print()

# o/p will be
# 1 3 5 7 9

start = 2
stop = -14
step = -2

number = range(start, stop, step)
for i in number:
    print(i, end=" ")
print()

# o/p will be
# 2 0 -2 -4 -6 -8 -10 -12


start = 0
stop = 50
step = -2

number = range(start, stop, step)
for i in number:
    print(i)

# Nothing will be printed

start = 0
stop = -50
step = -2

number = range(start, stop, step)
for i in number:
    print(i, end=" ")
print()

# 0 -2 -4 -6 -8 -10 -12 -14 -16 -18 -20 -22 -24 -26 -28 -30 -32 -34 -36 -38 -40 -42 -44 -46 -48

# seq[::n] to take the nth item from a list

number = range(0, 50)[::-2]
for i in number:
    print(i, end=" ")
print()

# 49 47 45 43 41 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 9 7 5 3 1

number = range(0, 50)[::2]
for i in number:
    print(i, end=" ")

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48