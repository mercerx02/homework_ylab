def zeros(n):
    result = 0
    while n != 0:
        result += n / 5
        n = n / 5
    return result


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7