def ft_null_count(number):
    count_nulls = 0
    if number < 0:
        number = -number

    while number > 0:
        if number % 10 == 0:
            count_nulls += 1
        number //= 10
    return count_nulls
