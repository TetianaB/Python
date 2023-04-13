# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# import math
# import time
#
#
# def square(s):
#     p = math.perm(s,s)
#     sq = math.pow(s,s)
#     diag = math.sqrt(2)*s
#     result = (p,sq, diag)
#     print(result)
#
# square(5)


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def my_employee(*kwargs):
#     for k,v in kwargs.items():
#         print(f'{k}: {v}')
#
# my_employee(name='John', last_name='Smith', age=35, position='web developer')

# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# employee(last_name='Popov', name='Max', age=40, position='web developer')

#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x>0,my_list )))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# print(reduce(lambda x,y: x * y, my_list))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# def my_decor(func):
#     def wrapper(args):
#         func(args)
#         print(time.perf_counter())
#     return wrapper
# @my_decor
# def test(name):
#     print(name*10)
#
# test('Tanya')
import time
def count_execution_time(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        exec_time = end - start
        print(f'{func.__name__} execution time is: {exec_time}')
        return result
    return wrapper

@count_execution_time
def greeting(name):
    return f'Hello {name}!'


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
