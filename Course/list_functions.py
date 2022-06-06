grocery = ["Soap","Sugar","Shampoo",10,25]
print(type(grocery))
print(len(grocery))
print(grocery[0])
print(grocery[0:4])
print(grocery[::-1])
numbers = [10,1,15,23]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
popped = numbers.pop()
print(popped)
numbers.append("100")
print(numbers)
print(type(numbers[-1]))
a = 1
b = 8
(a,b) = (b,a)
print(f'{a},{b}')
my_list = [10,20,30]
res = 5 * my_list
print(res)
