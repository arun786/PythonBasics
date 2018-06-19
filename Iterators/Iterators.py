string = '123456789'

for char in string:
    print(char, end=":")

    # o/p will be 1:2:3:4:5:6:7:8:9:

# internally it use iter

print()
string = '234567'
my_iterator = iter(string)

print(my_iterator)  # <str_iterator object at 0x000001D30C2BC710>

print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4
print(next(my_iterator))  # 5
print(next(my_iterator))  # 6
print(next(my_iterator))  # 7
