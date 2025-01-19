def function_with_uncommon_error(x, y):
    if x == 0:
        return float('inf') # Return positive infinity instead of raising an error
    elif y is None:
        return x #Return x if y is None 
    elif y == 0:
        return float('inf')
    else:
        return x / y