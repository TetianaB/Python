# text = int(input('Please enter the number here: '))
# count = 0
# while text !='stop':
#     num= int(text)
#     count+=num
#     text = input('If you want to stop just type "stop" instead of number: ')
#
# print(f'Sum is equiles: {count}')

# def repeat_str(repeat, string):
#     print(string*repeat)
#
# repeat_str(4,'Hello')

# def number_to_pwr(number, p):
#     for i in range (p+1):
#         n = number**i
#     print(n)
#
# number_to_pwr(3,2)

#Tuple

my_tuple = (1, 4, 'String', 'name', 'name', None, 25)
result = tuple([item for item in my_tuple if isinstance(item, int)])
print(result)

print(f'Sum is: {sum(result)}')
print(f'Maximum is: {max(result)}')
print(f'Minimum is: {min(result)}')
print(f'Length of my_tuple is: {len(my_tuple)}')
print(f'Length of my result is: {len(result)}')
print(my_tuple.index('String'))
print(my_tuple.count('name'))

for (index, item) in enumerate(my_tuple):
    print((index, item))

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i+=1

#NEsted list in tuple
# fruits = ('Apple', 'Banana', ['kiwi', 'watermelon'], 'orange')
#
# fruits[2][1] = 'cherry'
# print(fruits)

#swaping variables
# a = 5
# b = 10
# a,b = b,a
# print(f'a = {a}')
# print(f'b = {b}')