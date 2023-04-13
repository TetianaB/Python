import builtins

# l1 = [11,3,45,65,15,23]
# l = [12, 'sis', 23, 45.6, 'tet', 44]
# power = list(map(lambda x: x**x if isinstance(x, int) else x, l))
# print(power)
# filtered = list(filter(lambda x: not isinstance(x, float), l))
# print(filtered)
#
# from functools import reduce
# result = reduce(lambda x, y: x-y, l1)
# print(result)

# def my_decorator(func):
#     def wrapper(arg):
#         print("i am wrapper!")
#         func(arg)
#         print('Wrapped fuction')
#     return wrapper
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
#
# say_hello('Tanya')

# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#     return wrapper
#
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
# @sugar
# def coffee():
#     print('Coffee')
#
# coffee()

# import time
# bdate = 1971
# current_date = datetime.date.today()
# age = current_date.year - bdate
# current_month = current_date.month
# print(age)
# print(current_month)

import  modules
print(modules.hello('Same'))

from modules import sum as s

print(s(2,8))

print(dir(__builtins__))
print(f'Globals: {globals()}')
print(f'Locals: {locals()}')

