def ft_second_simple_max_num(number):
    max_digit = 0
    second_max_digit = 0
    temp = number
    while temp > 0:
        if max_digit < temp % 10:
            max_digit = temp % 10
        temp //= 10

    while number > 0:
        if max_digit >= number % 10 > second_max_digit:
            second_max_digit = number % 10
        number //= 10

    if second_max_digit == max_digit:
        return -1
    return second_max_digit
