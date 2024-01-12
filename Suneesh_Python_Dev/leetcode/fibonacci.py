import time


def fibonacci_recursion(num: int) -> int:
    if num <= 1:
        return num
    else:
        return fibonacci_recursion(num - 2) + fibonacci_recursion(num - 1)


def print_recursive_fibonacci(num: int) -> str:
    start_time = time.time()
    for i in range(num):
        print(f"i = {i + 1} : fib : = {fibonacci_recursion(i)}")
    end_time = time.time()
    return f"\nRecursion Time taken = {end_time - start_time}"


def fibonacci_non_recursion(num: int) -> int:
    if num == 0 or num == 1:
        return num

    a = 0
    b = 1
    while num >= 2:
        c = a + b
        a = b
        b = c
        num = num - 1

    return c


def print_fibonacci_dynamic_programming(num: int) -> str:
    start_time = time.time()
    for i in range(num):
        print(f"i = {i + 1} : fib : = {fibonacci_non_recursion(i)}")
    end_time = time.time()
    return f"\nDynamic Programming Time taken = {end_time - start_time}"


num = 30
recursion = print_recursive_fibonacci(num)
dynamic = print_fibonacci_dynamic_programming(num)
print(f"{recursion}\n{dynamic}")
