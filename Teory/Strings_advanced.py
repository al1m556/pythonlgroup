## Методы upper, lower, swapcase, capitalize
## Методы upper(), lower(), swapcase(), capitalize()
## выполняют преобразование регистра строки:

string1 = "Some text Here"

#функция .upper() делает все символы в строке символами с верхним регистром
print(string1.upper())

#функция .lower() соответственно наоборот

print(string1.lower())

#функция .swapcase() меняет верхний регистр на нижний и наоборот

print(string1.swapcase())

#функция .capitalize() преобразует первый символ в верхний регистр, а остальные в нижний

string1 = "sOmE TeXt HeRe"

print(string1.capitalize())

# Эти методы возвращают строку ввиде переменной, которую можно задать заново

string2 = string1.upper() 

print(string2)

##Метод count
##Метод count() используется для подсчета того, 
##сколько раз символ или подстрока встречаются в строке

print(string1.count("e"))

print(string1.count("t"))

print(string1.count("s"))

##Метод find
##Методу find() можно передать подстроку или символ, и он покажет, 
##на какой позиции находится первый символ подстроки (для первого совпадения):

string1 = "Lorem ipsum dolor sit amet"

find_string = string1.find("ip")

print(find_string)

print(string1[find_string::])

#Если совпадение не найдено, метод find возвращает -1.

##Метод replace
##Замена последовательности символов в 
##строке на другую последовательность (метод replace()):

string3 = "My name is Alexander"

string3 = string3.replace("Alexander", "Mark")

print(string3)

