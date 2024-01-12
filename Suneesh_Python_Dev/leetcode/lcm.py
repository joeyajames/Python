def lcm_method(a: int, b: int) -> int:
    if a > b:
        lcm = a
    else:
        lcm = b

    for i in range(a * b):
        if lcm % a == 0 and lcm % b == 0:
            break

        lcm = lcm + 1

    return lcm


res = lcm_method(4, 6)
print(res)

str_list = ["a",
            "b",
            "c",
            "d",
            "e"]

res = "".join(str_list)
print(res)
