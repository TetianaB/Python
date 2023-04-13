# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

usertext = input('What do you want to type? Please enter your sentence here: ')
howmany = int(input('how many times you want to repeat it? '))

for i in range(howmany):
    print(usertext)