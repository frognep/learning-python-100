from function import clear

clear()

# Playing with *args
# def add_numbers(*args):
#     # print(args[1])
#     total = 0
#     for n in args:
#         total += n
#     return total


# print(add_numbers(1, 2, 3, 4))

# **kwargs [keyword arguments]

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]

#     print(n)


# calculate(2, add=3, multiply=5)


# class Car:

#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")


# my_car = Car(make="Toyota", model="Camry")

# print(my_car.model)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)