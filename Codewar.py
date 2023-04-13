# def type_validation(variable, _type):
#     # your code here
#     a = type(variable)
#     if a == str(_type):
#         print ('True')
#     else:
#         print('False')
# type_validation(42, str)
import datetime
import math


# def nearest_sq(n):
#     x = int(math.sqrt(n))
#     y = int(x + 1)
#     z = int(x - 1)
#
#     if (n / x) == x:
#         print(n)
#     elif (n / x) != x and ((y ** 2) - n) >= (n - (z ** 2)):
#         print(z ** 2)
#     else:
#         print(y ** 2)
#
#
# nearest_sq(2)
#
# def valid_parentheses(paren_str):
#     c=[]
#     y = len(c)
#     for x in paren_str:
#         y=0
#         if x == '(' and x == ')':
#             c.append(x)
#             y = len(c)
#
#     if y%2==0:
#             print('True')
#     else:
#             print('False')
#
# valid_parentheses('((I )lobly (d)()))(')

# def missing(nums, s):
#    nums.sort()
#    print(nums)
#    s = s.split()
#    print(s)
#    s = ''.join(s)
#    print(s)
#
#    output = ''
#    for i in nums:
#        if i>= len(s):
#            print('No mission today')
#        else:
#            output+=s[i]
#    print(output)
#
# missing([0, 3, 5], "I love you")
#
# def capitalize(s, ind):
#     new = ''
#     for i in range(0, len(s)):
#         if i in ind:
#             new += s[i].upper()
#         else:
#             new += s[i].lower()
#     print(new)
#
#
# capitalize("abcdefhjk",[1,2,5])
# capitalize("abcdef",[1,2,5,100])

# def real_numbers(n):
#     l = []
#     for i in range(0, n+1):
#         if i%2 != 0 and i%3 != 0 and i%5 != 0:
#             l.append(i)
#     print(l)
#
# real_numbers(72)

# def sum_no_duplicates(l):
#     l = []
#     my_list2 = (sorted(set(my_list)))
#     s = math.sum(my_list)
#     print()

# def how_much_water(water, load, clothes):
#     result=0
#     if clothes > load * 2:
#         print('Too much clothes')
#     elif clothes <= load:
#         print('Not enough clothes')
#     else:
#         result = water * 1.1 ** (clothes - load)
#         print(float(round(result, 2)))
#
# # how_much_water(58,5,10)
#
# def number(bus_stops):
#     bus_stops=list(bus_stops)
#     y=0
#     z=0
#     for x in bus_stops:
#         y +=x [0]
#         z +=x [1]
#     print(y-z)
#
#
#
#
#
# number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])
# number([[10,0],[3,5],[5,8]])

# def count_consonants(text):
#     # text.split()
#     lst = []
#     abc = ['a','o', 'i', 'u', 'e']
#     for x in text:
#         x=x.lower()
#         if x.isalpha() and x not in abc:
#             lst.append(x)
#         else:
#             continue
#     print(len(set(lst)))


# def count_consonants(text):
#     lst = []
#     for x in text:
#         x=x.lower()
#         if x not in "auoie" and x.isalpha():
#             lst.append(x)
#         else:
#             continue
#     print(len(set(lst)))



    # print(len(set([i for i in text.lower() if i not in 'auoie' and i.isalpha()])))



# count_consonants('sillystring')
# #  7
# count_consonants('aeiou')
# # 0
# count_consonants('abcdefghijklmnopqrstuvwxyz')
# # , 21)
# count_consonants('Count my unique consonants!!')
# , 7)
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'M': 'Malware'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'M': 'Mike'}

# def alias_gen(f_name, l_name):
#     first_l = f_name[0].upper()
#     last_l = l_name[0].upper()
#     al = [first_l, last_l]
#
#     if first_l.isdigit() or last_l.isdigit():
#         print('Your name must start with a letter from A - Z.')
#     else:
#         for k in FIRST_NAME.keys():
#             if k == al[0]:
#                 a = FIRST_NAME.get(k)
#
#         for l in SURNAME.keys():
#             if l == al[1]:
#                 b = SURNAME.get(l)
#
#         print(a +' ' + b)


# def alias_gen(f_name, l_name):
#     al = [f_name[0], l_name[0]]
#     if f_name[0].isdigit() or l_name[0].isdigit():
#         print('Your name must start with a letter from A - Z.')
#     else:
#         for k in FIRST_NAME.keys():
#             if k == al[0]:
#                 a = FIRST_NAME.get(k)
#
#         for l in SURNAME.keys():
#             if l == al[1]:
#                 b = SURNAME.get(l)
#
#                 print(a +' ' + b)

# def alias_gen(f_name, l_name):
#     if f_name[0].isalpha() and l_name[0].isalpha():
#         print(f'{FIRST_NAME.get(f_name[0].upper())} {SURNAME.get(l_name[0].upper())}')
#     else:
#         print('Your name must start with a letter from A - Z.')
#
#
# alias_gen('Alex', 'Bloom')
# alias_gen('Mike', 'Millington')
# alias_gen('123Alex', 'Bloom')
import math
def min_min_max(arr):
    # l = list(arr)
    # minil = []
    for i in range(min(arr), max(arr)):
        if i not in arr:
            print([min(arr), i, max(arr)])



        # if i not in l and i > min(l):
        #     minimumAbsent = i
    # result = [list[min(l), min(minil), max(l)]
        #     print(minimumAbsent)






min_min_max([-1, 4, 5, -23, 24])
min_min_max([1, 3, -3, -2, 8, -1])


