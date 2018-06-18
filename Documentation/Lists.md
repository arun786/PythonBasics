# Lists

    firstway = [1, 4, 2, 3]
    secondway = list("12345")
    thirdway = sorted(firstway)
    print(firstway)
    print(secondway)
    print(thirdway)
    
    
    # [1, 4, 2, 3]
    # ['1', '2', '3', '4', '5']
    # [1, 2, 3, 4]

# == vs is

    number1 = [1, 2, 3]
    number2 = [1, 2, 3]
    
    if number1 == number2:
        print("Contents are the same")
    else:
        print("Contents are not the same")
    
    # the above will print Contents are the same
    
    if number1 is number2:
        print("Lists point to the same memory")
    else:
        print("Lists have different memory allocation")
    
        # the above will print, Lists have different memory allocation
    
    number3 = number1
    
    if number3 is number1:
        print("Lists point to the same memory")
    else:
        print("Lists point to different memory")
    
    # the above will print Lists point to the same memory

# Sorting a list

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

# Adding two lists

    odd = [1, 3, 5, 7]
    even = [2, 4, 6, 8]
    
    sum = [odd, even]
    print(sum)
    
    print()
    
    for outer in sum:
        print(outer)
        for inner in outer:
            print(inner)
