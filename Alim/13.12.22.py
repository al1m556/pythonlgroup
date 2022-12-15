# set1 = {1,2,3,4,5,5,4,3,2,1}

# print(set1, type(set1))

# set2 = set()

# print(type(set2))
# list1 = [1,2,3,4,5,6,'asd',123,444,0]
# set3 = set(list1)

# print(set3)

# str1 = 'some text here'

# set4 = set(str1)

# print(set4)

# set4.add(12)

# print(set4)


# set4.discard(' ')
# print(set4)

# set4.clear()
# print(set4)

# set5 = {1,2,3,4,5,6,7,8,9,10}

# set6 = {5,6,7,8,9,10,11,12,13,14,15}

# set_union = set5.union(set6)
# # set_union = set5|set6
# print(set_union)

# set_inter = set5.intersection(set6)

# print(set_inter)

# def to_set(bsdf):
#     set1 = set(bsdf)
#     return set1

# while True:
#     a = input('Хотите ввести список чисел или строку? /n spisok/stroka ')
#     if a == 'spisok':
#         j = int(input('Введи длину списка:'))
#         list1 = []
#         g = 1
#         while len(list1) < j:
#             f = int(input(f'Введите число номер {g}: '))
#             list1.append(f)
#             g +=1
        
#     elif a == 'stroka':
#         f = input('Введите строку: ')
#         break
#     else:
#         print('Введите еще раз')
#         continue

# answer1 = to_set(a)

# print(answer1)

# a = (3,5,34,23,4,3)

# def to_sort(a):
#     for i in a:
#         if type(i) == int:
#             vb = sorted(a)
#         else: 
#             vb = 'Вы ввели кортеж содержащий не только целые числа'
#     return vb

# answer = to_sort(a)
# print(answer)
# a = [2,34,2342,352,35]

# def min_max(a):
#     b = min(a)
#     c = max(a)
#     h = f'max is {c}, min is {b}'
#     return h
# print(min_max(a))

a = [2,34,2342,352,35]

def sieve(k):
    list.reverse(k)
    vv = set(k)
    vbncm = tuple(vv)
    return vbncm

print(sieve(a))

    