def ft_oct_num(number):
    p = 1
    d = 0
    while number > 0:
        d += number % 8 * p
        p *= 10
        number //= 8
    return d
