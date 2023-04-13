# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате:
# {num1} {operator) {num2) = {result}

number_1 = input('Your first number: ')
number_2 = input('Your second number: ')
result = int(number_1) + int(number_2)
result_str = str(result)
print(f'{number_1} + {number_2} = {result}')



2.5.
# C указанием каждого оператора в отдельном условии
try:
    num1 = int(input('Пожалуйста, введите первое число: '))
    num2 = int(input('Пожалуйста, введите второе число: '))
except ValueError as e:
    print(f'Введенное значение не является числом: {e}')
    sys.exit()
operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
if operator not in '+-*/%':
    print("Вы ввели не правильный оператор!")
    sys.exit()
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        sys.exit()
elif operator == '+':
    result = num1 + num2
elif operator == '*':
    result = num1 * num2
elif operator == '-':
    result = num1 - num2
elif operator == '%':
    result = num1 % num2
else:
    result = num1/num2
print(f'{num1} {operator} {num2} = {result}')

#C применением функции eval()

try:
    num1 = int(input('Пожалуйста, введите первое число: '))
    num2 = int(input('Пожалуйста, введите второе число: '))
except ValueError as e:
    print(f'Введенное значение не является числом: {e}')
    sys.exit()
operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
if operator not in '+-*/%':
    print("Вы ввели не правильный оператор!")
    sys.exit()
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
else:
    result = eval(f'{num1} {operator} {num2}')
    print(f'{num1} {operator} {num2} = {result}')