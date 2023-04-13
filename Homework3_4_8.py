# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1=[]
# family_2=[]
# family_1=input('Enter all the members separated by coma: ').split(',')
# print(list(family_1))
# family_2=input('Enter your family 2 separated by come: ').split(',')
# print(list(family_2))
# if len(family_2) > len(family_1):
#     print('This family is bigger: ', family_2)
# elif len(family_2) == len(family_1):
#     print('Equal')
# else:
#     print('This family1 is bigger:', family_1)


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

dic={'title' : 'Movie', 'director' : 'Hichkok', 'year' : '2019', 'budget' : '230000000', 'main_actor' : 'Kianu Reevs', 'slogan' : "Best movie"}
print(dic.keys())
print(dic.values())
print(dic.items())
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

print(set([1, 2, 3, 4, 5, 3, 2, 1]))

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      # - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))