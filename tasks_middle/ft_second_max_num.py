def ft_len_num(number):
    count_digits = 0
    if number < 0:
        number = -number
    while number > 0:
        count_digits += 1
        number //= 10
    return count_digits


def ft_second_max_num(number):
    max_digit = 0
    second_max_digit = 0
    temp = number

    while temp > 0:
        if max_digit < temp % 10:
            max_digit = temp % 10
        temp //= 10

    while number > 0:
        if max_digit > number % 10 > second_max_digit:
            second_max_digit = number % 10
        number //= 10

    return second_max_digit
