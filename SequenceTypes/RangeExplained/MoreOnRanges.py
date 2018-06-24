number1 = range(0, 5, 2)
number2 = range(0, 6, 2)

for i in number1:
    print(i, end=" ")  # 0 2 4
print()

if number1 == number2:  # this will print true
    print("true")
else:
    print("false")

print(list(number1))  # o/p will be [0,2,4]
print(list(number2))  # o/p will be [0,2,4]

decimals = range(0, 100)
my_range = decimals[3:40:3]

for i in my_range:
    print(i, end=",")  # this will print 3,6,9,12,15,18,21,24,27,30,33,36,39,

print()
decimals = range(0, 10)
my_range = decimals[3:40:3]

for i in my_range:
    print(i, end=":")  # this will print 3:6:9:

print()

r = range(0, 40)
for i in r[::2]:
    print(i, end="-")  # this will print 0-2-4-6-8-10-12-14-16-18-20-22-24-26-28-30-32-34-36-38-

print()

for i in r[::-2]:
    print(i, end=" ")  # this will print 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 9 7 5 3 1

# the above can be also written as
print()

for i in range(1, 30)[::5]:
    print(i, end=" ")  # this will print 1 6 11 16 21 26

backstring = 'egaugnal lufrewop yrev si nohtyp'
print()

print(backstring[::-1])  # python is very powerful language

for i in range(0, 10)[::-1]:
    print(i, end=" ")  # 9 8 7 6 5 4 3 2 1 0
print()
for i in range(0, 10, 1):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9
