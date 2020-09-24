def ft_len_num(number):
    count_digits = 0
    if number < 0:
        number = -number
    while number > 0:
        count_digits += 1
        number //= 10
    return count_digits
