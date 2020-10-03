"""
If we want to pass a large number of parameters to a function.
How will we do it ???
The answer is using *args(arguments) and *kwargs(keyworded arguments).

Without *args and and *kwargs we would be doing this like this :
def function_name(a,b,c,d):
    print(a,b,c,d)

function_name('Harry','Rohan','Bobby','Shiva')

We will be making variables for every incoming parameters.
This in turn will take a lot of time and memory and will be very hectic.
"""



"""Normal arguments must come before args and kwargs"""

def fun_args(normal,*args,**kwargs):
    print(type(args))
    print(normal)
    for iter in args:
        print(iter)

    print('\nNow I would like to meet some people : ')
    for key,value in kwargs.items():
        print(f'{key} is a {value}')
    print('')
    print(kwargs.keys())


name = ['Rohit','Harry','Rohan','Bobby','Shiva']
normal = 'I am a normal argument and the students are : '
kw = {'Rohan':'Student','Harry':'Programmer','Ronny':'Headboy','Shivam':'Cook'}

fun_args(normal,*name,**kw)




