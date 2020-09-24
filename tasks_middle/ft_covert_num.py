def ft_covert_num(number, s):
    p = 1
    d = 0
    while number > 0:
        d += number % s * p
        p *= 10
        number //= s
    return d
