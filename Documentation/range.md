# Range

    my_list = list(range(10))
    print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    even = list(range(0, 10, 2))
    odd = list(range(1, 10, 2))
    
    print(even)  # [0, 2, 4, 6, 8]
    print(odd)  # [1, 3, 5, 7, 9]
    
    my_list = 'abcdefghijklmnopqrstuvwxyz'
    print(my_list.index('e'))  # 4
    print(my_list[4])  # e
    
    small_decimals = range(0, 10)
    print(small_decimals)  # range(0,10)
    
    print(small_decimals.index(3))  # 3
    
    odd = range(1, 10000, 2)
    print(odd[985])  # 1971
    
    
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
    
    number1 = range(0, 5, 2)
    number2 = range(0, 6, 2)
    
    for i in number1:
        print(i, end=" ")  # 0 2 4
    print()
    
    if number1 == number2:  # this will print true
        print("true")
    else:
        print("false")
    
    print(list(number1))  # o/p will be [0,2,4]
    print(list(number2))  # o/p will be [0,2,4]
    
    decimals = range(0, 100)
    my_range = decimals[3:40:3]
    
    for i in my_range:
        print(i, end=",")  # this will print 3,6,9,12,15,18,21,24,27,30,33,36,39,
    
    print()
    decimals = range(0, 10)
    my_range = decimals[3:40:3]
    
    for i in my_range:
        print(i, end=":")  # this will print 3:6:9:
    
    print()
    
    r = range(0, 40)
    for i in r[::2]:
        print(i, end="-")  # this will print 0-2-4-6-8-10-12-14-16-18-20-22-24-26-28-30-32-34-36-38-
    
    print()
    
    
    for i in r[::-2]:
        print(i, end=" ")  # this will print 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 9 7 5 3 1
    
    # the above can be also written as
    print()
    
    for i in range(1, 30)[::5]:
        print(i, end=" ")  # this will print 1 6 11 16 21 26
    
    backstring = 'egaugnal lufrewop yrev si nohtyp'
    print()
    
    print(backstring[::-1])  # python is very powerful language
    
    for i in range(0, 10)[::-1]:
        print(i, end=" ")  # 9 8 7 6 5 4 3 2 1 0
    print()
    for i in range(0, 10, 1):
        print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9


## Understanding negative range

    start = 1
    stop = 10
    step = 2
    
    number = range(start, stop, step)
    
    for i in number:
        print(i, end=" ")
    print()
    
    # o/p will be
    # 1 3 5 7 9
    
    start = 2
    stop = -14
    step = -2
    
    number = range(start, stop, step)
    for i in number:
        print(i, end=" ")
    print()
    
    # o/p will be
    # 2 0 -2 -4 -6 -8 -10 -12
    
    
    start = 0
    stop = 50
    step = -2
    
    number = range(start, stop, step)
    for i in number:
        print(i)
    
    # Nothing will be printed
    
    start = 0
    stop = -50
    step = -2
    
    number = range(start, stop, step)
    for i in number:
        print(i, end=" ")
    print()
    
    # 0 -2 -4 -6 -8 -10 -12 -14 -16 -18 -20 -22 -24 -26 -28 -30 -32 -34 -36 -38 -40 -42 -44 -46 -48