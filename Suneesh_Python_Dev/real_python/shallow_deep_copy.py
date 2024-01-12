from copy import copy
from copy import deepcopy


def shallow_copy_from_copy_module():
    print("shallow_copy_from_copy_module()")
    a = [1, 2, 3.4e4]
    b = copy(a)
    print(id(a))
    print(id(b))

    print(a)
    a[1] = "fgf"
    print(b)

    print(id(a[0]) == id(b[0]))


def shallow_copy_copy():
    print("shallow_copy_copy()")
    a = [1, 2, 3.4e4]
    b = a.copy()

    print(id(a))
    print(id(b))

    print(a)
    a[1] = "fgf"
    print(b)

    print(id(a[0]) == id(b[0]))


def shallow_copy_slice():
    print("shallow_copy_slice()")
    a = [1, 2, 3.4e4]
    b = a[:]
    print(id(a))
    print(id(b))

    print(a)
    a[1] = "fgf"
    print(b)

    print(id(a[0]) == id(b[0]))


def deep_copy():
    print("deep_copy()")
    a = [1, 2, 3.4e4]
    b = deepcopy(a)
    print(id(a))
    print(id(b))

    print(a)
    a[1] = "fgf"
    print(b)

    print(id(a[0]) == id(b[0]))


shallow_copy_slice()
shallow_copy_copy()
shallow_copy_from_copy_module()
deep_copy()
