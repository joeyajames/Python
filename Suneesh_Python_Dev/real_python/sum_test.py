def my_sum(res, ele):
    return res + ele


res = 0
for ele in [1, 2, 3, 4]:
    res = my_sum(res, ele)

print(res)

print(sum([1, 2, 3, 4, 5]))
