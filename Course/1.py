x = [1,2,3,4,5]
del x[3]
print(x)

myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2}
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print("I am able to code is Python now")
'''
usr_ip = int(input("Enter number:"))
num1 = 12 if usr_ip==10 else 13
print(num1)
'''
pets = ['cats', 'dogs', 'rabbits', 'hamsters']
for index, name in enumerate(pets):
	print(index, name)

try:
    ans = 12/0
    print("Hello world")
except:
    print("Error occured:Dont divide by 0")
