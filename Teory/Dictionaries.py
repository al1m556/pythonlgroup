#Словари             | Dictionaries

# Пример словаря
person_details = {
    'first_name': 'Tony',
    'last_name': 'Macaroni',
    'age': 26,
    'job': 'Reporter',
}

print(person_details)

# Можно записывать и так

person_details = {"first_name": "Tony", 'last_name': 'Macaroni','age': 26,'job': 'Reporter'}

print(person_details)

# Для того, чтобы получить значение из словаря, надо обратиться 
# по ключу, таким же образом, как это было в списках,
# только вместо номера будет использоваться ключ

print(person_details['first_name'])
print(person_details['last_name'])

#Таким же образом можно изменять значение ключа в словаре

person_details['first_name'] = "Kaleb"


print(person_details['first_name'])

#Аналогичным образом можно добавить новую пару ключ-значение

person_details["eyes"] = "brown"

print(person_details)

# Функция sorted сортирует ключи словаря по возрастанию и 
# возвращает новый список с отсортированными ключами


print(sorted(person_details))