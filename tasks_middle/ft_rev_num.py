def ft_rev_num(number):
    rev = 0
    if number < 0:
        number = -number
        while number > 0:
            digit = number % 10
            rev = rev * 10 + digit
            number //= 10
        return -rev

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10
    return rev
