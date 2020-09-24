def ft_multi_num(number):
    multi_digits = 1
    if number < 0:
        number = -number

    while number > 0:
        multi_digits *= (number % 10)
        number //= 10
    return multi_digits
