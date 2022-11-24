str1 = "Some text"

str2 = "another text"

str3 = str1 + ' ' + str2 

print(str3)

print(str3[7])

liter1 = str3[8]

print(liter1)

print(str3[4:])

print(str3[:15])

print(str3[4:15])

print(str3[-2])

print(str3[3:12:2])

print(str3[::-1])

str4 = str3*5

print(str4)

# str_input = input('Введите имя: ')

# print('Ваше имя: ',str_input)

# num1 = int(input('Введите число: '))

# print(num1, type(num1))

url1 = 'www.CalTetch.kz/teAcher[]/lesson'

num2 = 1

url2 = 'www.caltetch.kz/teacher[' + str(num2)+ ']/lesson'

print(url2)

url3 = f'www.caltetch.kz/teacher[{num2}]/lesson'

print(url3)

str4 = url1.upper()

print(str4)
# .lower()

print(url1.lower())
# .swapcase()
print(url1.swapcase())

# .capitalize()
print(url1.capitalize())

print(url1.count('C'))

result1 = url1.find('Cal')
result2 = url1.find('.kz')

print(result1)

print(url1[result1:result2])

replace1 = url1.replace('CalTetch','anekdot')

print(replace1)

str5 = 'fhlajksdghadfjgadkfjgaier\n adsfasdgdfhjg'

print(str5)


str6 = ''' akdylkafjg
fjkhbsgret
jlvnsbl123748565
/.[p
sdfg4
''klfdkgls'
'''

print(str6)