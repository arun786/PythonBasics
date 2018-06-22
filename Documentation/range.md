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