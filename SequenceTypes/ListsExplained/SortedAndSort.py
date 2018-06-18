number1 = [6, 8, 10, 2, 4]

number2 = sorted(number1)  # sorted returns a new list

print(number1)  # 6,8,10,2,4
print(number2)  # 2,4,6,8,10

if number1 is number2:
    print("Lists point to the same memory")
else:
    print("Different memory location")

number1.sort()
print(number1)

# to reverse a list

reverseNumber = sorted(number1, reverse=True)
print(reverseNumber)

number5 = [1, 2, 3, 48, 9]
number5.sort(reverse=True)
print(number5)
