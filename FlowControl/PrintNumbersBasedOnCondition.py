for i in range(0, 20):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
# use with continue

print('---------')
for i in range(0, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
