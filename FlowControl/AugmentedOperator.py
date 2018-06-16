number = "9,123,456,789,256,978,345"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]  # augmented +=

newNumber = int(cleanedNumber)
print("This number is {}".format(newNumber))

# Augmented

x = 23
x += 1
print(x)  # 24

x -= 4
print(x)  # 20

x *= 5
print(x)  # 100

x /= 4
print(x)  # 25.0

x **= 2
print(x)  # 625.0

x %= 60
print(x)
