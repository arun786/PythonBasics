age = 24

# to convert int to string we use str(age).
print("My age is " + str(age) + " years")

# Replace field
print("My age is {0} years".format(age))

# Replace Field
print("There are {0} days in {1}, {2}, {3},{4},{5},{6},{7}"
      .format(31, "January", "March", "May", "July", "August", "October", "December"))

# replacement fields with Triple quotes
print("""
January : {2}
February : {0}
March : {2}
April : {1}
May : {2}
June : {1}
July : {2}
August : {2}
September : {1}
October : {2}
November : {1}
December : {2}""".format(28, 30, 31))

# String formatting deprecated used in Python 2
print("My age is %d years" % age)
print("My age is %d %s %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print('No %2d squared is %3d and Cubed is %4d' % (i, i ** 2, i ** 3))

# output will be
# No  1 squared is   1 and Cubed is    1
# No  2 squared is   4 and Cubed is    8
# No  3 squared is   9 and Cubed is   27
# No  4 squared is  16 and Cubed is   64
# No  5 squared is  25 and Cubed is  125
# No  6 squared is  36 and Cubed is  216
# No  7 squared is  49 and Cubed is  343
# No  8 squared is  64 and Cubed is  512
# No  9 squared is  81 and Cubed is  729
# No 10 squared is 100 and Cubed is 1000
# No 11 squared is 121 and Cubed is 1331

# value precision
print("value of pi is %12f" % (22 / 7))

# output will be
# value of pi is     3.142857

print("Value of pi is %12.50f" % (22 / 7))
# output will be
# Value of pi is 3.14285714285714279370154144999105483293533325195312
