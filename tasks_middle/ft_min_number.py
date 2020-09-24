def ft_min_number(number):
    min_digit = (number % 10)
    while number > 0:
        if min_digit < (number % 10):
            min_digit = (number % 10)
        number //= 10
    return min_digit
