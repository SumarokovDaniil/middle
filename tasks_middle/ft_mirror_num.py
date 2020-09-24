def ft_mirror_num(number):
    temp = number
    rev = 0
    if number < 0:
        number = -number
        temp = number
        rev = 0
        while number > 0:
            digit = number % 10
            rev = rev * 10 + digit
            number //= 10

        if rev == temp:
            return True
        return False

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number //= 10

    if rev == temp:
        return True
    return False
