num = ["10","20","30","40","50"]

num = list(map(int, num))

num = list(map(lambda x: x**2, num))
print(num)
print(num[2])
print(type(num[2]))
