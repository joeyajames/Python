import math


def is_positive(number):
    return number >= 0


def sanitized_sqrt(numbers):
    f = filter(is_positive, numbers)
    print(id(f))
    print(type(f))
    return list(map(math.sqrt, f))


print(sanitized_sqrt([9, 16, -1]))
