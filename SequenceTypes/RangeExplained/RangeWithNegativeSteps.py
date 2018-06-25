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