import random

print("Hello Buddy")

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

def append_to_list(value, my_list=None):
    if my_list is None:
        my_list=[]
    my_list.append(value)
    return my_list

def greet(*names, **details):
    for name in names:
        print(f"Hello {name}")
    print("Details : ", details)

greet("Habib", "Sahil", age=19, city="Karachi")


def apply_func(f,x):
    return f(x)

square= lambda n: n*n
print(apply_func(square,5))

nums =[1,2,3,4,5,6]
squared=list(map(lambda x: x*x, nums))
print(squared)