# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются
# столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается
# високосным (1200, 2000)

user_inp = int(input('Enter your year here: '))
number1 = user_inp % 4
number2 = user_inp % 400
number3 = user_inp % 100

if number3 == 0:
    if number2 == 0:
        print('This year is leap year')
    else:
        print('This year is not leap year')

elif number3 != 0 and number1 == 0:
    print('This year is leap year')
else:
    print( 'This year is not leap year')