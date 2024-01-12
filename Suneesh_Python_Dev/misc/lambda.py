def square(x):
    return x*x

square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)
