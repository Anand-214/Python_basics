dict1 = {"key1":"value1","key1":"value2"}
print(dict1)
list1 = ['a','b','c','d','r','u']
'''print(id(list1[0]))
print(id(list1[1]))
print(id(list1[2]))'''
list2 = [1,2,3,4,5,6,7]
#list1.extend(list2)
#print(list1)
list3 = list2.copy()
list3[3] = 100
print(list2)
print(list3)

