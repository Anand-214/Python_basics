'''list1 = [1,2,3,4]
list2 = list1
print(f"list1: {list1}")
print(f"list2: {list2}")
list2[1] = 100
print(f"list1: {list1}")
print(f"list2: {list2}")     #here list1 and list2 both changed because = will directly share the same memory location between these two.No copy will be created.
#we use .copy for shallow copy and import copy for deep copy

'''
list3 =  [10,20,30,40] 
list4 = list3      #shallow copy will not refer the same memory location. A new compound object will be created.
print(f"list3: {list3}")
print(f"list4: {list4}")
list4[1] = 1000
print(f"list3: {list3}")
print(f"list4: {list4}")
print(id(list4))
print(id(list3))

'''import copy
list_1 = ["a","b","c","d"]
list_2 = list_1.deepcopy()
print(list_1)
print(list_2)
'''
