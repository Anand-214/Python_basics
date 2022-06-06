def gen(n):
	for i in range(n):
		yield(i)
def __repr__():
	print("This is a generator object and will yield always.")
g = gen(5)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


