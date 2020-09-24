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


def ft_rev_covert_num(number, s):
    p = 1
    d = 0
    while number > 0:
        d += number % s * p
        p *= 10
        number //= s
    return ft_rev_num(d)
