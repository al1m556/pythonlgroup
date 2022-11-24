list1 = []
num1 = 10
list1 = [1,2,3,4,'str',2.0, True, num1, [5,4,7,8]]

print(list1)

print(list1[4])
print(list1[-1])

list2 = list1[-1]
print(list2[-1])

print(list1[-1][3])

list1[6] = 'Number1'

print(list1)

list3 = []

list3.append(87)
list3.append('str')
list3.append(12.4)

print(list3)

list3.insert(1, '123')
print(list3)

list3.remove(87)
print(list3)

list3.pop(1)
print(list3)

value = list3.pop(-1)

print(list3, value)

list4 = [1,2,5,7,9,3,6,8,22,5,7,9,3346,8,27,899,0]

print(list4[3:10])
print(list4)

list4.sort()
print(list4[::-1])

list5 = ['str1', 'Text','another text', 'Mark']

list5.sort()

print(list5)

list4.extend(list5)

print(list4)

print(list4.count(8))