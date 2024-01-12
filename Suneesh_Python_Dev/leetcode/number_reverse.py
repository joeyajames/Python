def reverse_number(x: int) -> int:
    if x > 2 ** 31 - 1 or x < -1 * 2 ** 31:
        return 0

    negative = False
    if x < 0:
        negative = True

    res = 0
    x = abs(x)
    while x > 0:
        temp = x % 10
        res = res * 10 + temp
        x = int(x / 10)

    if negative:
        res = -1 * res

    return res


print(reverse_number(1534236469))
