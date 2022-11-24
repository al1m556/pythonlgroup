dict1 = {'name': 'Alexander', 'age':25}

print(dict1)
print(dict1['name'])
name = dict1['name']

dict1['profession'] = 'programmer'

print(dict1)

del dict1['age']

print(dict1)

sorted_dict = sorted(dict1)

print(sorted_dict)

dict2 = dict1
dict3 = dict1.copy()

print(dict1, dict2,dict3)

dict1['name'] = 'Mark'

print(dict1,dict2,dict3)

dict2 = []
dict2.clear()



result1 = dict1.get('name',1)

print(result1)

result2 = dict1.setdefault('winner',False)

print(result2, dict1)


keys1 = dict1.keys()

values1 = dict1.values()

items1 = dict1.items()

print(keys1,values1,items1)


dict4 = {'asdfasd':0,'qwerteg':'asdfa'}

dict1.update(dict4)

print(dict1)


# des = input('А или Б? ')

# if des == 'А':
#     print('Вы ввели букву А ')
# elif des == "Б":
#     print('Вы ввели букву Б ')
# else: 
#     print('Вы ввели не ту букву!')

a = 3

if a <2:
    print(a+1)
elif a <10:
    print(a+10) 
if a < 5:
    print(a+5)       
    