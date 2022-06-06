print("map function")
my_list = ["1","2","3","4"]

my_list = list(map(int, my_list))
print(my_list)

nums =["10","20","30","40"]
nums = set(map(int, nums))
nums = list(map(lambda x:x**2, nums))
print(nums)

'''
new_list = [1,2,3,4,5]
str_list = []
sq = lambda x:x*x
for i in range(len(new_list)):
    str_list[i] = sq(i)
print(str_list)
'''
list_1 = [1,2,3,4,5,6,7,8,9]

def greater_than_5(num):
    return num>=5

def sq_gtr_thn_20(num):
	if (num**2) > 30:
		return num

res_list = list(filter(greater_than_5, list_1))
print(res_list)

sq_list = set(filter(sq_gtr_thn_20, list_1))
print(sq_list)
print(*"Hello")	
