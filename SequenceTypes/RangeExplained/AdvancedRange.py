sevens = range(0, 1000000, 7)
x = int(input("Please enter a number : "))
if x in sevens:
    print("Number {} is present in the range".format(x))
else:
    print("Number {} is not present in the range".format(x))

# to print multiplication table of 3

number = range(3,31,3)
for i in number:
    print(i)

# O/p will be
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30