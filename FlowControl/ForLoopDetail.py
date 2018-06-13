number = '1,2,3,4,567,789,21,90,34'
for i in range(0, len(number)):
    print(number[i], end='')
print()
print('-----------------')
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
print()
print('--------------')
number = '1,2,3,4,567,789,21,90,34'
cleanednumber = ''
for char in number:
    if char in '0123456789':
        cleanednumber += char

newnumber = int(cleanednumber)

print(newnumber)
print()

