o = range(0,100,4)
print(o) # range(0,100,4)

p = o[::5]
print(p) # range(0,100,20)

for i in p:
    print(i,end=" ") # 0 20 40 60 80

print()

print(o)

p = o[::-5]
print(p) # range(96, -4, -20)

for i in p:
    print(i,end=" ") # 96 76 56 36 16

o = range(100,0,-20)
print()

for i in o:
    print(i, end=" ")