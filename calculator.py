import math
import statistics

def add(x: float, y: float) -> float:
    return x + y

def divide(x,y):
    return x/y

def factorial(x):
    return math.factorial(x)

def sin(x):
    N = 20
    for i in range(N):
        sine = 0
        sine += (-1)**i * (x**(2*N + 1))/(math.factorial(2*N + 1))
        return sine

def mean(x): #must have list as input
    return statistics.mean(x)

def var(x): #must have list as input
    return statistics.variance(x)
