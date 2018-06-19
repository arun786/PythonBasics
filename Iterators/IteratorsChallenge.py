name = 'qwerty'
size = len(name)

my_name = iter(name)

for char in range(0, size):
    print(next(my_name))

day = ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun']
my_day = iter(day)

for i in range(0, len(day)):
    print(next(my_day))
