def ft_max_num(number):
    max_digit = 0
    if number < 0:
        number = -number
    while number > 0:
        if max_digit < (number % 10):
            max_digit = (number % 10)
        number //= 10
    return max_digit
