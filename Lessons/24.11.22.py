num1 = 0

while num1 <= 10:
    print(num1)
    num1 = num1 + 1 # num1 +=1 

list1 = [1,3,6,2,7,9,3,7,0,4,6,88]
sum1 = 0

for elem1 in list1:
    print(elem1)
    sum1 += elem1

print(sum1)

str1 = ' some text here'

for elem2 in str1:
    print(elem2)

person_details = {
    'first_name': 'Tony',
    'last_name': 'Macaroni',
    'age': 26,
    'job': 'Reporter',
}

for elem3 in person_details:
    print(elem3, person_details[elem3])


list2 = [5,1,9,23,35,8,9,0]

for elem4 in list2:
    if elem4 == 9:
        print('Here is number nine!')
        continue
    elif elem4 >40:
        break
    elif elem4 <40:
        pass
    print(elem4)  
else: 
    print('Well done!')
print('cycle end')    


for i in range(-5,11,2):
    print(i)