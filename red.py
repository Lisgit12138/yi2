from functools import reduce

a = [1,2,3]
def func(a,b):
    return str(a)+str(b)
print(reduce(func,a))