def list_comprehension_change(numbers):
    numbers = [int(num) for num in numbers]
    print(f"id : {id(numbers)} / value = {numbers}")


def in_place_change(numbers):
    for index, value in enumerate(numbers):
        numbers[index] = int(value)

    print(f"id : {id(numbers)} / value = {numbers}")


numbers = ["1", "2", "3", "4", "5"]
print(f"id : {id(numbers)} / value = {numbers}")

list_comprehension_change(numbers)
in_place_change(numbers)

print([num ** 2 for num in [1, 2, 3, 4]])

print(list(map(lambda num: num ** 2, [1, 2, 3, 4])))
