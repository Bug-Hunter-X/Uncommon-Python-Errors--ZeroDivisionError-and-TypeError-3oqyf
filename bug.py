def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    elif y is None:
        return x + y # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
    else:
        return x / y