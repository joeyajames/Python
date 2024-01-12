def display(set1):
    print(f"Type = {type(set1)}, id = {id(set1)} , value = {set1}")


def func1(*args):
    display(args)
    [display(ele) for ele in args]


def func2(**args):
    display(args)
    [display(ele) for ele in args]


func1("asas", True, 1, 2, 3, 4)

func2(
    arg1="abc",
    arg2=2,
    arg3=4734,
    arg4=True
)
