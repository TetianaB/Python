#Напишите программу, которая проверяет здоровье персонажа в игре.
#Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

user_question = int(input('How do you feel on scale from 5 to -5? Answer here: '))
if -5 <= user_question <= 5:
    print('False')
elif user_question > 5 or  user_question < -5:
    print('Wrong number! Please use from -5 to 5 only')
else:
    print('True')

# Напишите программу, которая проверяет является ли введенное число четным. Если да,
# выведите на экран текст “Четное”, а иначе - “Нечетное”

usr_input = int(input('Enter your number here: '))
number_type = usr_input % 2
if number_type == 0:
    print(f'This number {usr_input} is even')
else:
    print('This number is odd!')

number = int(input('Введите любое число: '))
if number%2:
    print('Нечетное')
else:
    print('Четное')