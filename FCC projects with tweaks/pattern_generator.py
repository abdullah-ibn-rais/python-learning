def number_pattern(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Argument must be an integer value."
    if a < 1 or b < 1:
        return "Argument must be an integer greater than 0."
    return ' '.join([str(number) for number in range(1,a+1,b)])
    
    
print(number_pattern(10,3))

