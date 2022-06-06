list1 = [1,2,3,4,5,6,7,8,9,10]
sq = lambda x : x**2
eve = lambda x : x%2!=0

list_new = del.list1(10)
print(list_new)
lst = list(filter(eve,(map(sq, list1))))
print(lst)

def recursive_fact (x):
	if x == 1:
		return 1
	else:
		return x * recursive_fact(x-1)

res = recursive_fact(4)
print(res)
