def ft_sum_num(number):
    sum_digits = 0
    if number < 0:
        number = -number

    while number > 0:
        sum_digits += (number % 10)
        number //= 10
    return sum_digits
