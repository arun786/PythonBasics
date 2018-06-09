# Python basics 

## Basics

    _author_ = 'dev'
    print('Hello, World!')
    print(1 + 2)
    print(7 * 6)
    print()
    print("The End")
    print("Python's Strings are easy to use")
    print('We can add "Quotes" to Strings')
    print("Hello" + "World")
    
    greeting = "Hello"
    name = "Arun"
    
    print(greeting + name)
    print(greeting + ' ' + name)
    
    # Comments

## Input Function

    _author_ = 'dev'
    greeting = "Hello"
    name = input("Please enter your name")
    print(greeting + ' ' + name)

## Split Function

    splitSpring = "This String has been\nsplit over \nseveral \ntimes"
    print(splitSpring)
    
    # output will be
    # This String has been
    # split over
    # several
    # times

## Tabbed Function

    tabbedString = "1\t2\t3\t4\t5"
    print(tabbedString)
    
    # output will be
    # 1	2	3	4	5

## Escape Function

    print('This is Adwiti\'s laptop')
    print("We can use quotes inside quotes \" ...")
    
    # Output will be
    # This is Adwiti's laptop
    # We can use quotes inside quotes " ...
   
## Triple Quotes

    tripleQuotesFunction = """This is string which has got Arun's laptop and uses " in the middle of the sentence"""
    print(tripleQuotesFunction)
    
    splitUsingTripleQuotes ="""This is
    India
    having diverse cultures"""
    
    print(splitUsingTripleQuotes)
    
    # output will be
    # This is string which has got Arun's laptop and uses " in the middle of the sentence
    # This is
    # India
    # having diverse cultures

# Variables

## Integer

    a = 12
    b = 4
    print(a + b)  # 16
    print(a - b)  # 8
    print(a * b)  # 48
    print(a / b)  # 3.0
    print(a // b)  # 3
    print(a % b)  # 0
    
    bun_price = 2.40
    money = 15
    print(money // bun_price) # 6.0
    print(money / bun_price) # 6.25
    
# To print a String with int

    we use str() function
    
    age = 24
    
    # to convert int to string we use str(age).
    print("My age is " + str(age) + " years")
    
# Replace Fields

    print("May age is {0} years".format(24))
    
    print("There are {0} days in {1}, {2}, {3},{4},{5},{6},{7}"
          .format(31, "January", "March", "May", "July", "August", "October", "December"))
          
# replacement fields with Triple quotes
    print("""
    January : {2}
    February : {0}
    March : {2}
    April : {1}
    May : {2}
    June : {1}
    July : {2}
    August : {2}
    September : {1}
    October : {2}
    November : {1}
    December : {2}""".format(28, 30, 31))
    
# String formatting deprecated was used in python 2
    print("My age is %d years" % age)
    print("My age is %d %s %d %s" % (age, "years", 6, "months"))
    
    for i in range(1, 12):
        print('No %2d squared is %3d and Cubed is %4d' % (i, i ** 2, i ** 3))
    
    # output will be
    # No  1 squared is   1 and Cubed is    1
    # No  2 squared is   4 and Cubed is    8
    # No  3 squared is   9 and Cubed is   27
    # No  4 squared is  16 and Cubed is   64
    # No  5 squared is  25 and Cubed is  125
    # No  6 squared is  36 and Cubed is  216
    # No  7 squared is  49 and Cubed is  343
    # No  8 squared is  64 and Cubed is  512
    # No  9 squared is  81 and Cubed is  729
    # No 10 squared is 100 and Cubed is 1000
    # No 11 squared is 121 and Cubed is 1331

# value precision
    print("value of pi is %12f" % (22 / 7))

    # output will be
    # value of pi is     3.142857

    print("Value of pi is %12.50f" % (22 / 7))
    # output will be
    # Value of pi is 3.14285714285714279370154144999105483293533325195312

# If Else Function

    print("Enter a number in between 1 and 10")
    guess = int(input())
    
    if guess < 5:
        print("Please enter a higher value")
        guess = int(input())
        if guess == 5:
            print("You have guessed it right")
        else:
            print("Sorry you are wrong")
    elif guess > 5:
        print("Please enter a lower value")
        guess = int(input())
        if guess == 5:
            print("You have guessed it right")
        else:
            print("Sorry you are wrong")
    else:
        print("You are right the first time")
    
    # the above code had duplication, lets improve it
    
    print("Please enter again for better code")
    guess = int(input())
    
    if guess != 5:
        if guess > 5:
            print("Please guess it lower")
        else:
            print("Please guess it higher")
    
        guess = int(input())
    
        if guess == 5:
            print("you guessed it right")
        else:
            print("Sorry you are wrong")
    else:
        print("You guessed it correct the first time")

# Complex if else

    age = int(input("Enter your age : "))
    if (age > 15) and (age < 65):
        print("Have a good day at work")
    else:
        print("Please enjoy your free time")
    
    if 15 < age < 65:
        print("Have a good day at work")
    else:
        print("Please enjoy your free time")
    
    age = int(input("Please enter the age again"))
    if (age < 16) or (age > 64):
        print("Please enjoy your free time")
    else:
        print("Have a good day at work")
