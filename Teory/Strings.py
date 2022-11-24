#Строки              | Strings
one_string = "Hello world"
print(one_string)

#Суммирование строк
##Строки можно суммировать. Тогда они объединяются в одну строку

s1 = "Hello"
s2 = 'World'
space = " "
text = s1 + space + s2  
print(text)

#Умножение строки на число
##Строку можно умножать на число. В этом случае, строка повторяется указанное количество раз

text = text * 5 
print(text)

##Форматирование текста

some_text = "\n Some text here \n and some text here"

print(some_text)

#Текс за тройными кавычками

text_big = """
Lorem ipsum dolor sit amet, 
      consectetur adipiscing elit,
sed do eiusmod tempor incididunt
 #####@@!$%^!@#$%^&*()ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat.
""" 

print(text_big)

#  Вывод символа по индексу
## Нумерация всех символов в строке идет с нуля.
## Но, если нужно обратиться к какому-то по счету символу, 
## начиная с конца, то можно указывать отрицательные значения.

text  = "here we have some text with numbers 1234567890"
print(text[5])

print(text[-1])
#   Вывод диапазона символов
##  Кроме обращения к конкретному символу, можно делать срезы строк,
##  указав диапазон номеров (срез выполняется по второе число, не включая его)

print(text[5:30])

print(text[:30])

print(text[50:])

#Вывод диапазона символов с шагом 

print(text[1::3])

print(text[::2])

#   Вывод символов в обратном порядке
##  Срезы также можно использовать для получения строки в обратном порядке

print(text[::-1])