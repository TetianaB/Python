# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
from typing import List

my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
list_2 = []
for n in list_1:
    if type(n)==int:
        list_2.append(n)
print(sum(list_2))
list_3=[]
for s in list_1:
    if isinstance(s,str) and 'a' in s:
        list_3.append(s)
print(list_3)


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

a=['cat', 'dog', 'horse', 'cow']
a=tuple(a)
print(type(a))
