#Списки              | Lists

#Пример простейшего списка

list_of_numbers = [1, 2, 3]
print(list_of_numbers)

#Пример списка с различными типами данных 
list_of_stuff = [1, 'item', 1.2, True, ['list', 'in', 'list']]
print(list_of_stuff)

#Пример создания списка и добавления в него новых элементов 
some_list = []

some_list.append('This is a box with text')
print(some_list)

some_list.append('This is another different box with text')
print(some_list)

#   Еще один пример создания списка
#   Создание списка с помощью функции list()

list1 = list("Some text")
print(list1)

# Так как список - это упорядоченный тип данных, 
# то, как и в строках, в списках можно обращаться 
# к элементу по номеру, делать срезы

print(list1[1])

print(list1[:5])

print(list1[3:])

print(list1[-1])

print(list1[::-1])

#Так как списки изменяемые, элементы списка можно менять

list2 = list("12345678890")

list2[5] = 13

print(list2)