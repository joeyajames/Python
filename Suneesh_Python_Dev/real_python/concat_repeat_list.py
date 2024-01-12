def list_repeat():
    a = [1, 2, 3]
    c = a * 2
    print('a={}'.format(id(a)))
    print('c={}'.format(id(c)))
    print(c)
    c *= 3
    print('c={}'.format(id(c)))
    print(c)


def list_concat():
    a = [1, 2, 3]
    b = ["x", "y", "z"]
    c = a + b
    print('a={}'.format(id(a)))
    print('b={}'.format(id(b)))
    print('c={}'.format(id(c)))

    c += [99, 88, 77]
    print('c={}'.format(id(c)))
    print(c)


# list_concat()
list_repeat()
