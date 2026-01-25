"""
A demo of how to do newton/raphson in python
"""

def square(x):
    return x*x

def third(x):
    return x*x*x

def identity(x):
    return x

def newton_raphson(f, initial_guess=1.0, max_iterations=1000, dx=0.001, precision=0.001):
    x=initial_guess
    i=0
    while i<max_iterations:
        y=f(x)
        derivitive=(f(x+dx)-f(x-dx))/(2*dx)
        if abs(derivitive) < precision:
            return x
        x+=-y/derivitive
        # print(f"x is {x}")
        i+=1
    return None

result=newton_raphson(identity)
if result is None:
    print("couldnt find solution")
else:
    print(f"found solution {result}")
