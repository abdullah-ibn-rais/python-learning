def outerfunc():
    a=5
    b=''
    def innerfunc():
        nonlocal b
        global c
        b=5
        c=10

    innerfunc()    
    return b
print(outerfunc())
print(c)
