def ft_pow(number, s):
    previous = number
    if s > 0:
        for i in range(s - 1):
            number *= previous
        return number
    elif s == 0:
        return 1
    for i in range(number):
        number /= previous
    return number


def ft_rev_bin_num(number):
    temp = number
    bin_number = 0
    count_digits = 0
    while temp > 0:
        temp //= 10
        count_digits += 1
    for digit in range(count_digits):
        bin_number += number % 10 * ft_pow(2, digit)
        number //= 10
    return bin_number
