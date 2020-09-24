def ft_min_number(number):
    min_digit = number % 10
    while number > 0:
        digit = number % 10
        if min_digit > digit:
            min_digit = digit
        number //= 10
    return min_digit
