list1 = [1,2,3,4,5,6]
list2 = list1
#for i in range(len(list1)):
print("List 2 is :",list2)
print(type(list2))
print(type(list1.append(10)))
t = (1,2,3,[4,5,6])
l1 = list(t)
l1.pop()
l1.append([7,8,9])
print(l1)
