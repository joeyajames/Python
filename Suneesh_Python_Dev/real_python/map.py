numbers = ["1", "2", "3", "4", "5"]


def function(number):
    print(number)


# function(numbers)
l1 = list(map(function, numbers))
# print(l)

[function(num) for num in numbers]
