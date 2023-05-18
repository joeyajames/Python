import random

def __is_sorted(_list):
    if len(_list) == 0 or len(_list) == 1:
        return True
    prev_item = _list[0]
    for next_item in _list[1:]:
        if prev_item > next_item:
            return False
        prev_item = next_item
    return True

def __shuffle(_list):
    for i in range(len(_list)):
        position_1 = random.randint(0,len(_list)-1)
        position_2 = random.randint(0,len(_list)-1)
        _list[position_1], _list[position_2] = _list[position_2], _list[position_1]

def random_sort(_list):
    while not __is_sorted(_list):
        __shuffle(_list)

_list = [0, 8, 2, 1, 5, 6, 4, 7, 3]
print(f'list before sort: {_list}')
random_sort(_list)
print(f'list after sort: {_list}')
