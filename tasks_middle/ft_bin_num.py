def ft_bin_num(number):
    p = 1
    d = 0
    while number > 0:
        d += number % 2 * p
        p *= 10
        number //= 2
    return d
