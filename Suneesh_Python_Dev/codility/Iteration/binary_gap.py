def display(element):
    print(f"Type = {type(element)}, id = {id(element)} , value = {element}")


def get_binary(number: int) -> str:
    return str(bin(number)).split('b')[1]


def binary_gap(binary_number: str) -> int:
    res = 0
    count = []
    location = 0
    str_to_process = binary_number[location:]
    while location <= len(binary_number) and str_to_process != '':
        if str_to_process != '':
            try:
                location = str_to_process.index('1')
            except ValueError:
                pass
            str_to_process = str_to_process[location + 1:]
            if (location > 0):
                count.append(location)
            # print(count)

    if len(count) > 0:
        res = max(count)
    return res


for num in range(1, 1000):
    binarynum = get_binary(num)
    print(f"Number{num} , Binary = {binarynum}, binary gap = {binary_gap(binarynum)}")
