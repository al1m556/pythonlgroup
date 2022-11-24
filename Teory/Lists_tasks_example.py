# 1

list1 = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

print(list1)

# 2 

list1.append("Zero")
print(list1)

# 3 

list1.insert(12,137)
print(list1)

# 4

list1.append(["Some","list","here"])
print(list1)

#5

elem1 = list1[10]
elem1 = list1[list1.index(9)]
print(elem1)

#6

list1.remove(0)
print(list1)
###
list1.pop(10)
print(list1)

# 7 

print(list1.count(1))