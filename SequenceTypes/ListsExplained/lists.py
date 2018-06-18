ipAddress = input("Enter Ip address...")
print('Number of periods in ipaddress is {}'.format(ipAddress.count('.')))

# List

print("States")
states = ['Maharastra', 'Megahalaya', 'Assam', 'Kerela']

for state in states:
    print(state)

print("Sum of odd and even")

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]

number = odd + even
number.sort()  # to sort a number, .sort() sorts on the same list
print(number)

print('-------------')
newNumber = odd + even
sorted_number = sorted(newNumber)  # sort a number using sorted returns a new object

if sorted_number == number:  # == checks the content of the list
    print("The numbers are equal")
else:
    print("The numbers are not equal")

print('-------------')

if sorted_number is number:
    print("The variables point to the same memory")
else:
    print("The variables do not point to the same memory")
