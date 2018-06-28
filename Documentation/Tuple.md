# Tuple    
    
    t = "a", "b", "c"  # this is a tuple
    print(t)
    
    print(t[0])
    print(t[1])
    print(t[2])
    
    print("a", "b", "c")
    
    # t[3] = "z" # tuple is immutable and cannot be assigned
    
    # in case of a list, we can reassign
    
    t1 = ["a", "b", "c"]  # this is a list
    print(t1)
    
    t1[0] = "z"
    print(t1)  # List is mutable
    
    t = "a", t[1], "c"  # This will work since both point to the same object
    print(t)
    
    # Tuples are designed to hold heterogenous items
    
    t2 = "arun", 23
    print(t2)
    
    # unpacking tuple
    
    arun = "arun", 23, "scottsdale"
    name, age, address = arun
    print(name)  # arun
    print(age)  # 23
    print(address)  # scottsdale
    

    # We can do the below in python
    
    a, b = 12, 13
    print(a, b)  # 12,13
    print("a has the value {}".format(a))
    print("b has the value {}".format(b))
    # o/p will be
    # a has the value 12
    # b has the value 13
    
    a, b = b, a
    print("a has the value {}".format(a))
    print("b has the value {}".format(b))
    # o/p will be
    # a has the value 13
    # b has the value 12