from functools import reduce


my_list = ["1","2","3","4","5"]
list_1 = [5,6,7,8,9,10]

my_list = list(map(int, my_list))

print(type(my_list[0]))
print(my_list)

def gtr_than_2(num):
    return num>2

new_list = list(filter(gtr_than_2, my_list))
print(new_list)

res = reduce(lambda x,y: x*y, my_list)
print(res)
