def sequence_generator(sequnce):
    for item in sequnce:
        yield item


for item in sequence_generator([1, 2, 3, 4]):
    print(item)


def g():
    for item in [1, 2, 3]:
        yield item


aa = g()
print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
