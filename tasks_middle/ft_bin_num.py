def ft_bin_num(number):
    d = 0
    while number > 0:
        d = d * 10 + number % 10
        number //= 2
    return d
