def my_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a real positive 'x' and a negative integer 'y'"
    return res


print(my_func(3.2, -3))
