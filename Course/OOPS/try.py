'''a = -12/6
print(a)

dict1 = {}
dict2 = dict() 
print(type(dict1))
print(type(dict2))

tup = (1,2,3,4,[4,5,6])
l1 = list(tup)
l1[4] = [10,11,12]
l2 = tuple(l1)
print(l2)

#SHALLOW COPY
list1 = [1,2,3,4,5]
list2 = list1
print(id(list1))
print(id(list2))
list1[1] = 100
print(list2)

##DEEP COPY
import copy
list3 = [10,20,30,40]
list4 = copy.deepcopy(list3)
print(list4)
list3[3] = 1000
print(list3)
print(list4)
print(id(list3))
print(id(list4))

dict_1 = {"key1":"value1","key2":"value2"}
#for x,y in enumerate(dict_1):
for x,y in dict_1.items():
    print(y)
	
square = lambda x : x*x
'''


