# #1 i 2
# sum = 0
# for i in range(0,101):
#      sum += i
# print(sum)
# #3
# for i in range (1,498):
#      if i % 2 == 0:
#          print(i)

# list1 = [1,2,5,12,14,48,256,17]
# for i in list1:
#      print(i)
# else: list1.append("list1 over")

# print(list1)

# ##4

# ##5
# for int1 in range(0,6):
#     result = (int1*117 + 87)//13 * (21**int1)
#     print(result)

##2 term 1 task
import random
random_int = random.randint(1,100)
print(random_int)

b = 10
while b >=1:
    i = int(input("введите число"))
    if i == random_int:
        print('Верно')
    elif i < random_int:
        print('число меньше чем вписанное')
    elif i > random_int:
        print('число больше чем вписанное')
    else:
        print('Неверно,введите "ЧИСЛО"')
        continue
    print(f'осталось {b} попыток ')
    
    




    